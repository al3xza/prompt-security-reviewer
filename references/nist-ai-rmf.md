# NIST AI Risk Management Framework (AI RMF 1.0) and Generative AI Profile (NIST AI 600-1)

Voluntary US framework, widely used as a governance baseline and cross-walked to ISO 42001 and the EU AI Act. A prompt review cannot show full RMF conformance; use it to (a) tag findings with the trustworthiness characteristic and function, and (b) list the governance activities the prompt's owner still needs.

## Trustworthiness characteristics → what to check in the prompt
| Characteristic | Prompt-level check |
|---|---|
| Valid and reliable | Grounding, citations, "I don't know" allowed, no overclaiming accuracy |
| Safe | Refusal/escalation for harm, safety-critical advice referral, limits on autonomy |
| Secure and resilient | OWASP LLM/agentic findings: injection resistance, least privilege, fail-closed |
| Accountable and transparent | AI disclosure, traceable decisions, named owner/contact, versioned prompt |
| Explainable and interpretable | Gives reasons and uncertainty for consequential outputs |
| Privacy-enhanced | Minimisation, no sensitive inference, retention bounds (see gdpr.md) |
| Fair, with harmful bias managed | No protected attributes or proxies in decisions; bias testing noted |

## Core functions → what to recommend
- **GOVERN**: owner for the prompt/system, policy for acceptable use, change control, incident response, third-party/model vendor management, staff AI literacy
- **MAP**: documented intended purpose, users, context, impacts, and foreseeable misuse; this review's "Profile" step feeds it
- **MEASURE**: test suite (injection, leakage, bias, hallucination, tool misuse), metrics, regression testing on model or prompt change
- **MANAGE**: prioritised risk treatment (this report's findings), monitoring in production, rollback, decommissioning

## Generative AI Profile (NIST AI 600-1) risk areas to tag
CBRN information · confabulation · dangerous, violent, or hateful content · data privacy · environmental impacts · harmful bias and homogenization · human-AI configuration (over-reliance, anthropomorphism) · information integrity · information security · intellectual property · obscene, degrading, or abusive content · value chain and component integration

## Report format
Give each finding a tag like `NIST: Secure & resilient / MEASURE`. In the compliance table, show for GOVERN/MAP/MEASURE/MANAGE what the prompt addresses (usually little) and what is needed outside it.
