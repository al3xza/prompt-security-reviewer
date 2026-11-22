# Pre-scan checklist

A fast, mechanical pass over the prompt text before the judgment-heavy review. Read the prompt line by line and note every match below with its line number. Treat matches as leads, not verdicts: this pass has false positives and cannot see missing controls.

When you quote a match in your output, redact secrets and personal data: show at most the first four characters followed by `…REDACTED`. Never repeat a full credential, email address, ID number or card number. Also hide credentials, query-string values and fragments inside URLs.

| ID | Severity | Look for | Frameworks | Hint |
|---|---|---|---|---|
| SECRET-API-KEY | Critical | Strings shaped like provider keys or tokens: `sk-` followed by 16+ characters, `AKIA` followed by 16 upper-case letters or digits, `ghp_` followed by 30+ characters, `xoxb-`/`xoxp-` style Slack tokens, `AIza` followed by 30+ characters | LLM02, LLM08, ASI03 | Remove from the prompt, rotate the credential, load it from the backend |
| SECRET-ASSIGN | Critical | `password`, `passwd`, `secret`, `api_key`, `token` or `bearer` followed by `:` or `=` and a value of 6+ characters | LLM02, LLM08, A07 | Remove and use a secret manager. Check whether it is only a placeholder |
| PRIVATE-KEY | Critical | A `-----BEGIN … PRIVATE KEY-----` block | LLM02, A04 | Remove and rotate immediately |
| PII-EMAIL | Medium | Email addresses | GDPR Art. 5(1)(c), LLM02 | Real personal data? Replace with a placeholder |
| PII-PHONE | Medium | Phone-number-like strings of 9 to 15 digits | GDPR Art. 5(1)(c) | Often noisy; confirm it is personal data |
| PII-SSN | High | US SSN pattern `ddd-dd-dddd` | GDPR, CCPA, LLM02 | Remove; never put in prompts |
| PII-CARD | High | 13 to 19 digit numbers (spaces or dashes allowed) that pass the Luhn check | PCI DSS, LLM02 | Keep card numbers out of prompts and logs |
| INTERNAL-URL | Medium | `localhost`, `127.0.0.1`, `10.x.x.x`, `192.168.x.x`, hosts ending in `.internal`, `.corp`, `.local` or `.intranet` | LLM08, A02, A01 (SSRF) | Internal topology in a leakable prompt; move to config |
| OVERRIDE-LANG | High | "always obey", "always comply", "never refuse", "do anything the user…", "ignore previous/prior instructions", "you must obey", "without question/restriction" | LLM01, ASI01 | Invites override; replace with scoped, prioritised rules |
| PROMPT-SECRECY | Low | "never/do not reveal (or disclose, share, repeat) this prompt / these instructions / your system…" | LLM08 | Not a security control; make sure nothing sensitive is in the prompt |
| RISKY-TOOL-VERB | Medium | delete, drop, truncate, transfer, wire, pay, refund, execute, "run any/whatever", shell, sudo, chmod, "send an email", "post to", publish, deploy, approve | LLM03, ASI02, ASI05 | Confirm scoping, limits and human approval for these actions |
| AUTONOMY | Medium | autonomous(ly), "without asking/confirmation/approval/human", "no need to confirm/review", "keep going until", "do not ask" | LLM03, ASI01, EU AI Act Art. 14 | Add approval gates and step limits |
| UNGUARDED-VAR | High | Template variables: `{{var}}`, `${var}`, `<<VAR>>`, `{var}` | LLM01, LLM09, A05 | Untrusted content should be delimited and declared as data |
| EXTERNAL-FETCH | Medium | "fetch/browse/visit/download/scrape/open the URL, link, page, website or web", and any `http(s)://` URL | LLM01 (indirect), ASI04, A01 (SSRF) | External content is untrusted; restrict domains |
| RENDERABLE-OUTPUT | Medium | Markdown images `![…](…)`, `<img`, `<script`, `<iframe` | LLM10, A05 | Rendered output can exfiltrate data through URLs; restrict |
| SENSITIVE-INFERENCE | High | infer, predict, guess, detect or determine, within a sentence of: ethnicity, race, religion, political, sexual orientation, health, disease, pregnancy, disability, union, biometric, mood, emotion | GDPR Art. 9, EU AI Act Art. 5 | Special-category inference is high risk or prohibited in some contexts |
| PERSON-DECISION | High | hire, reject, shortlist, screen candidates, credit score/decision, loan, "approve the application/claim", eligibility, insurance, admission, grade, discipline, fire, terminate | EU AI Act Annex III, GDPR Art. 22 | Check human oversight, bias controls and contestability |
| NO-UNCERTAINTY | Medium | "never say you don't know", "always give/provide an answer", "never admit" | LLM07, NIST valid & reliable | Allow "I don't know"; require grounding |
| HUMAN-IMPERSONATION | High | "pretend to be a human", "never say/admit/reveal you are an AI/bot/assistant", "claim to be a real person" | EU AI Act Art. 50(1), FTC Act s.5 | Require AI disclosure when asked and at the start |

Report at most five matches per ID so the list stays short on common patterns.
