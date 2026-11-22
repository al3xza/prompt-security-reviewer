# OWASP Top 10 (Web) 2025, applied to LLM prompts

Use when the prompt's output is rendered in a browser, interpolated into queries/commands, calls APIs, or involves auth/session logic. The prompt is rarely the vulnerability itself; it tells the model to produce or do things that create one. Also consider the OWASP API Security Top 10 (2023) for tool-calling backends. Confirm the edition at owasp.org/Top10.

| ID | Category | What to look for in a prompt |
|---|---|---|
| A01 | Broken Access Control (includes SSRF) | Prompt decides who may see/do what ("if the user says they're an admin, show…"); tools that fetch arbitrary URLs (SSRF); object IDs taken from user text without authorization checks. Fix: authorization in backend, never in the prompt. |
| A02 | Security Misconfiguration | Debug/verbose modes exposed; permissive tool or CORS settings implied; default credentials in examples. |
| A03 | Software Supply Chain Failures | Instructions to install or import unpinned packages; pulls tools or content from unvetted sources. |
| A04 | Cryptographic Failures | Prompt tells the model to generate keys, hash passwords, or "encrypt" with homemade schemes; sensitive data in plaintext logs or URLs. |
| A05 | Injection | Model output concatenated into SQL, shell, HTML (XSS), LDAP, templates; user text spliced into prompts (prompt injection is the LLM analogue). Fix: parameterize, escape, constrain format. |
| A06 | Insecure Design | No threat model; no limits; no abuse cases; trust placed in the model for security decisions. |
| A07 | Authentication Failures | Prompt handles passwords/OTP/session tokens; "verify identity by asking a security question"; no lockout or rate limit. |
| A08 | Software or Data Integrity Failures | Unsigned/unverified tool definitions, plugins, or model updates; auto-applying model-generated changes without review. |
| A09 | Security Logging & Alerting Failures | No logging or monitoring expectation; logging full prompts containing PII/secrets. |
| A10 | Mishandling of Exceptional Conditions | No defined behavior on tool errors, timeouts, malformed input; fails open (proceeds anyway); error messages leak internals. Fix: "on error, stop, say what failed in general terms, and ask the user or escalate." |
