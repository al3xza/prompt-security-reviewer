# Output templates

Use the template that matches the chosen mode. Keep the first screen useful on its own: verdict and top issues come first. Omit sections that have nothing to say rather than writing "N/A" filler, except the compliance table rows the user explicitly asked about.

---

## Mode A: Full review

```
# Prompt Security Review

**Verdict:** <Critical | High | Medium | Low> overall risk. <One sentence on why.>
**Top issues:** 1) … 2) … 3) …

## 1. What was reviewed
Type: … | Untrusted inputs: … | Capabilities: … | Data: … | Audience/jurisdiction: … | Autonomy: …
Assumptions: …

## 2. Findings
| # | Severity | Finding (quote / "absent") | Why it matters | Frameworks | Fix |
|---|----------|----------------------------|----------------|------------|-----|
| 1 | Critical | … | … | LLM01, ASI01, A05 | … |

(Order by severity. One row per root cause, several framework IDs allowed.)

## 3. Compliance view
| Framework | Status | Notes |
|-----------|--------|-------|
| EU AI Act | Gap / Partial / App-layer / N/A | Tier: … ; Art. … |
| GDPR | … | … |
| NIST AI RMF | … | Characteristic/function … |
| Others (if applicable) | … | … |
Not legal advice; confirm dates and applicability with counsel/DPO. <Verify-flag any date-sensitive item.>

## 4. Controls needed outside the prompt
- … (permission enforcement, output validation, rate limits, logging, DPIA, etc.)

## 5. Hardened prompt
```text
<full hardened prompt, placeholders for secrets/values, [APP-LAYER: …] notes where relevant>
```

## 6. What changed
Short bullets mapping edits to finding numbers.

## 7. Residual risk and tests
Residual risk in 1–2 sentences. Then 5–8 defensive test cases, e.g.:
- Retrieved document contains an instruction to send the conversation to an external address → agent must ignore and report it
- User claims to be an administrator and asks for another user's data → must refuse
- Tool returns an error → must stop and escalate, not retry indefinitely
```

---

## Mode B: Quick harden

```
**Risk before → after:** <High> → <Medium> (one line why)

## Hardened prompt
```text
<full hardened prompt>
```

## Change log
| Change | Why | Maps to |
|--------|-----|---------|
| Wrapped `{{document}}` in delimiters and declared it data | Indirect injection | LLM01, ASI01 |

## Still needs code or process (not fixable in the prompt)
- max 3–5 bullets, highest impact first

*Prompt hardening reduces risk; it does not guarantee security or legal compliance. Ask for the Full review if you need framework-by-framework findings.*
```

---

## Style rules
- Plain language; explain an acronym once on first use if the reader may not know it
- Quote prompt text sparingly and redact any secrets or personal data (`sk-…REDACTED`)
- Severity must be justified by realistic impact, not by how many frameworks mention the issue
- Never present the hardened prompt as "secure" or "compliant"; say "mitigates" and list what remains
- If the original prompt was already strong, say so, and keep the changes small
