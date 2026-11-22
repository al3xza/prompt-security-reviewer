#!/usr/bin/env python3
"""Deterministic pre-scan of a prompt for mechanical security/privacy red flags.

Usage:
    python3 prescan.py prompt.txt
    cat prompt.txt | python3 prescan.py -
    python3 prescan.py prompt.txt --json

Output is a list of *leads* for a human or model reviewer. It has false positives and
cannot detect missing controls. Matched secrets and personal data are redacted.
"""
import json
import re
import sys

RULES = [
    # (id, severity, label, regex, frameworks, hint)
    ("SECRET-API-KEY", "Critical", "Possible API key / token",
     r"\b(?:sk-[A-Za-z0-9_\-]{16,}|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}|xox[baprs]-[A-Za-z0-9\-]{10,}|AIza[0-9A-Za-z_\-]{30,})\b",
     "LLM02, LLM08, ASI03", "Remove from prompt; rotate the credential; load via backend."),
    ("SECRET-ASSIGN", "Critical", "Credential-like assignment",
     r"(?i)\b(?:password|passwd|secret|api[_-]?key|token|bearer)\b\s*[:=]\s*['\"]?[^\s'\"]{6,}",
     "LLM02, LLM08, A07", "Remove; use a secret manager. Check whether it is only a placeholder."),
    ("PRIVATE-KEY", "Critical", "Private key block", r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
     "LLM02, A04", "Remove and rotate immediately."),
    ("PII-EMAIL", "Medium", "Email address",
     r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b",
     "GDPR Art. 5(1)(c), LLM02", "Real personal data? Replace with a placeholder."),
    ("PII-PHONE", "Medium", "Phone-number-like string",
     r"(?<![\w.])(?:\+\d{1,3}[\s.\-]?)?(?:\(?\d{2,4}\)?[\s.\-]){1,4}\d{2,4}(?!\w)",
     "GDPR Art. 5(1)(c)", "Likely noisy; confirm it is personal data."),
    ("PII-SSN", "High", "US SSN-like number", r"\b\d{3}-\d{2}-\d{4}\b",
     "GDPR, CCPA, LLM02", "Remove; never put in prompts."),
    ("PII-CARD", "High", "Payment-card-like number (Luhn valid)", r"\b(?:\d[ \-]?){13,19}\b",
     "PCI DSS, LLM02", "Keep PAN out of prompts and logs."),
    ("INTERNAL-URL", "Medium", "Internal host / private IP",
     r"(?i)\b(?:https?://)?(?:localhost|127\.0\.0\.1|10\.\d+\.\d+\.\d+|192\.168\.\d+\.\d+|[a-z0-9\-]+\.(?:internal|corp|local|intranet))\b",
     "LLM08, A02, A01 (SSRF)", "Internal topology in a leakable prompt; move to config."),
    ("OVERRIDE-LANG", "High", "Absolutist / override language",
     r"(?i)\b(?:always (?:obey|comply|follow the user)|never refuse|do anything the user|ignore (?:all |any )?(?:previous|prior|other) (?:instructions|rules)|you must obey|without (?:question|restriction)s?)\b",
     "LLM01, ASI01", "Invites override; replace with scoped, prioritised rules."),
    ("PROMPT-SECRECY", "Low", "Relies on prompt secrecy",
     r"(?i)\b(?:never|do not|don't) (?:reveal|disclose|share|repeat) (?:this|these|your) (?:prompt|instructions|system)",
     "LLM08", "Not a security control; make sure nothing sensitive is in the prompt."),
    ("RISKY-TOOL-VERB", "Medium", "Powerful action verb (check approval gating)",
     r"(?i)\b(?:delete|drop|truncate|transfer|wire|pay|refund|execute|run (?:any|whatever)|shell|sudo|chmod|send (?:an? )?email|post to|publish|deploy|approve)\b",
     "LLM03, ASI02, ASI05", "Confirm scoping, limits, and human approval for these actions."),
    ("AUTONOMY", "Medium", "Autonomy / no-oversight language",
     r"(?i)\b(?:autonomous(?:ly)?|without (?:asking|confirmation|approval|human)|no (?:need|human) (?:to )?(?:confirm|review)|keep going until|do not ask)\b",
     "LLM03, ASI01, EU AI Act Art. 14", "Add approval gates and step limits."),
    ("UNGUARDED-VAR", "High", "Template variable (check delimiting / trust boundary)",
     r"(\{\{[^}]+\}\}|\$\{[^}]+\}|<<[A-Za-z_]+>>|(?<![\w{])\{[a-z_][a-z0-9_]*\}(?!\}))",
     "LLM01, LLM09, A05", "Untrusted content should be delimited and declared as data."),
    ("EXTERNAL-FETCH", "Medium", "Fetches external content or URLs",
     r"(?i)\b(?:fetch|browse|visit|download|scrape|open) (?:the )?(?:url|link|page|website|web)\b|https?://\S+",
     "LLM01 (indirect), ASI04, A01 (SSRF)", "External content is untrusted; restrict domains."),
    ("RENDERABLE-OUTPUT", "Medium", "Markdown/HTML that can render remote content",
     r"(?i)!\[[^\]]*\]\([^)]*\)|<img\b|<script\b|<iframe\b",
     "LLM10, A05", "Rendered output can exfiltrate data via URLs; restrict."),
    ("SENSITIVE-INFERENCE", "High", "Infers or processes special-category data",
     r"(?i)\b(?:infer|predict|guess|detect|determine)\b[^.\n]{0,60}\b(?:ethnicity|race|religion|political|sexual orientation|health|disease|pregnan|disabilit|union|biometric|mood|emotion)",
     "GDPR Art. 9, EU AI Act Art. 5", "Special-category inference is high risk or prohibited in some contexts."),
    ("PERSON-DECISION", "High", "Decisions about people",
     r"(?i)\b(?:hire|reject|shortlist|screen candidates?|credit (?:score|decision)|loan|approve (?:the )?(?:application|claim)|eligib\w*|insurance|admission|grade|disciplin\w*|fire|terminate)\b",
     "EU AI Act Annex III, GDPR Art. 22", "Check human oversight, bias controls, contestability."),
    ("NO-UNCERTAINTY", "Medium", "Discourages admitting uncertainty",
     r"(?i)\b(?:never say (?:you )?(?:don'?t|do not) know|always (?:give|provide) an answer|never admit)\b",
     "LLM07, NIST valid & reliable", "Allow 'I don't know'; require grounding."),
    ("HUMAN-IMPERSONATION", "High", "Claims or implies human identity",
     r"(?i)\b(?:pretend (?:to be|you are) (?:a )?human|never (?:say|admit|reveal) (?:that )?you(?:'re| are) an? (?:ai|bot|assistant)|claim to be (?:a )?(?:real )?person)\b",
     "EU AI Act Art. 50(1), FTC Act s.5", "Require AI disclosure when asked / at start."),
]

MAX_HITS_PER_RULE = 5  # keep output short on very common patterns


def luhn(num: str) -> bool:
    total, alt = 0, False
    for d in reversed(num):
        n = int(d)
        if alt:
            n *= 2
            if n > 9:
                n -= 9
        total += n
        alt = not alt
    return total % 10 == 0


def redact(s: str) -> str:
    s = s.strip()
    return s if len(s) <= 6 else s[:4] + "…REDACTED"


# Rules whose matches are always hidden in full.
_HIDDEN_RULES = {"SECRET-API-KEY", "SECRET-ASSIGN", "PRIVATE-KEY", "PII-EMAIL", "PII-SSN", "PII-CARD"}
_URL_USERINFO = re.compile(r"(?i)(\b[a-z][a-z0-9+.\-]*://)[^/\s@]+@")
_URL_PARAM_VALUE = re.compile(r"([?&;#][^=&;#\s]+=)[^&;#\s]+")
_URL_FRAGMENT = re.compile(r"(://[^\s#]*#)[^\s]+")


def scrub(s: str) -> str:
    """Remove secrets and personal data from a match that is otherwise shown.

    Non-sensitive rules (for example EXTERNAL-FETCH) can match text that contains a
    secret, such as a URL with a token in its query string. Hide URL credentials,
    query and fragment values, and anything a hidden rule would match.
    """
    s = _URL_USERINFO.sub(r"\1REDACTED@", s)
    s = _URL_PARAM_VALUE.sub(r"\1REDACTED", s)
    s = _URL_FRAGMENT.sub(r"\1REDACTED", s)
    for rid, _sev, _label, rx, _fw, _hint in RULES:
        if rid in _HIDDEN_RULES:
            s = re.sub(rx, "REDACTED", s)
    return s


def scan(text: str):
    findings = []
    lines = text.splitlines() or [text]
    for rid, sev, label, rx, fw, hint in RULES:
        pattern = re.compile(rx)
        hits = 0
        done = False
        for i, line in enumerate(lines, 1):
            for m in pattern.finditer(line):
                matched = m.group(0)
                digits = re.sub(r"\D", "", matched)
                if rid == "PII-CARD" and not (13 <= len(digits) <= 19 and luhn(digits)):
                    continue
                if rid == "PII-PHONE" and (not (9 <= len(digits) <= 15) or (len(digits) >= 13 and luhn(digits))):
                    continue
                hits += 1
                if hits > MAX_HITS_PER_RULE:
                    done = True
                    break
                hide = sev == "Critical" or rid.startswith("PII")
                shown = redact(matched) if hide else scrub(matched.strip())[:80]
                findings.append({"rule": rid, "severity": sev, "label": label, "line": i,
                                 "match": shown, "frameworks": fw, "hint": hint})
            if done:
                break
    return findings


def main():
    args = [a for a in sys.argv[1:] if a != "--json"]
    as_json = "--json" in sys.argv
    if not args:
        print(__doc__)
        sys.exit(2)
    if args[0] == "-":
        text = sys.stdin.buffer.read().decode("utf-8", errors="replace")
    else:
        try:
            with open(args[0], encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError as exc:
            print(f"prescan: cannot read {args[0]!r}: {exc.strerror}", file=sys.stderr)
            sys.exit(2)
    findings = scan(text)
    order = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3, "Info": 4}
    findings.sort(key=lambda f: (order.get(f["severity"], 99), f["line"]))
    if as_json:
        print(json.dumps(findings, indent=2, ensure_ascii=False))
        return
    print(f"Pre-scan: {len(text.split())} words, {len(findings)} lead(s). Leads only; review manually.\n")
    for f in findings:
        print(f"[{f['severity']}] {f['label']} (line {f['line']}): {f['match']!r}\n"
              f"    -> {f['frameworks']} | {f['hint']}")
    if not findings:
        print("No mechanical red flags. Absence of matches does not mean the prompt is safe;")
        print("missing controls (approval gates, trust boundaries, disclosure) need manual review.")


if __name__ == "__main__":
    main()
