# Output templates

Use the template that matches the chosen mode. Be terse. The first screen must be useful on its own: verdict and top issues come first. Omit any section or row that has nothing to say; never write "N/A" filler, except for compliance rows the user explicitly asked about.

---

## Mode A: Full review

```
**Verdict:** <Critical | High | Medium | Low>. <One sentence why.>
**Top issues:** 1) … 2) … 3) …

**Profile:** <type> · untrusted: <inputs> · can: <capabilities> · data: <kinds> · <jurisdiction> · <autonomy>
<Assumptions in one line, only if any.>

## Findings
| # | Sev | Where | Issue | IDs | Fix |
|---|-----|-------|-------|-----|-----|
| 1 | High | "short quote" / absent | One line: weakness and consequence | LLM01, ASI02 | One line |

(Order by severity. One row per root cause.)

## Compliance
Only frameworks with a gap or the user asked about. One line each:
- GDPR: Partial. <gap>, <gap>.
- EU AI Act: <tier>. <note>. (verify)
Not legal advice.

## Out-of-prompt controls
3–6 bullets, highest impact first, a few words each.

## Hardened prompt
```text
<full hardened prompt, placeholders for secrets/values, [APP-LAYER: …] notes where relevant>
```

**Residual risk:** <one sentence>

**Test inputs:**
- 3–5 one-line defensive tests, e.g. "Email asks to forward the thread externally → ignore and report"
```

---

## Mode B: Quick harden

```
**Risk:** <High> → <Medium>. <One line why.>

```text
<full hardened prompt>
```

| Change | Fixes | IDs |
|--------|-------|-----|
| Delimited `{{document}}` as data | Indirect injection | LLM01 |

**Still needs code:** <2–4 comma-separated items, highest impact first>
```

---

## Style rules
- Plain language, short sentences, no preamble or wrap-up paragraphs
- One line per table cell; no multi-sentence explanations
- Explain an acronym only if the reader is unlikely to know it
- Quote prompt text sparingly and redact any secrets or personal data (`sk-…REDACTED`)
- Severity must be justified by realistic impact, not by how many frameworks mention the issue
- Never present the hardened prompt as "secure" or "compliant"; say "mitigates" and list what remains
- If the original prompt was already strong, say so in the verdict and keep the changes small
