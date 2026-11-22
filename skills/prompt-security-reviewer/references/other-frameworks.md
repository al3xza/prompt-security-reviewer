# Other frameworks (load only when relevant)

Mark all as "verify current text/status" in reports. Cite IDs only when confident; otherwise name the technique or control family.

## MITRE ATLAS (adversary tactics and techniques for AI systems)
Use to phrase findings as attacker behavior and to build test cases. Relevant technique families: LLM prompt injection (direct/indirect), LLM jailbreak, extraction of the system prompt ("meta prompt extraction"), LLM data leakage, poisoning of data or RAG sources, abuse of plugins/tools, exfiltration via inference API or rendered output. Confirm technique IDs at atlas.mitre.org before citing numerically.

## ISO/IEC 42001:2023 (AI management system) and ISO/IEC 23894 (AI risk management guidance)
Use for organizational assurance: policy, roles, risk assessment, impact assessment, data and lifecycle controls, supplier management, monitoring, continual improvement. A prompt review contributes evidence to risk assessment and operational controls; list missing governance items (owner, change control, testing records).

## US privacy and AI laws
- **CCPA/CPRA (California)**: notice at collection, right to know/delete/correct/opt out of sale or sharing, limits on sensitive personal information; regulations on automated decision-making technology and risk assessments have been phased in, so check current status. Flag profiling and sensitive-data use.
- **Colorado AI Act (SB 24-205)** and other state AI/automated-decision laws: duties for "high-risk" consequential decisions (employment, lending, housing, health, education, insurance). The effective date was delayed; verify status.
- **COPPA / state children's codes**: users under 13 (or minors under state codes). Flag any data collection or personalization targeted at kids.
- **FTC Act Section 5**: deceptive claims about AI capability, undisclosed AI personas.

## Sector-specific
- **HIPAA (US health)**: PHI in prompts or logs; need BAA with model vendor; minimum necessary standard; no PHI in few-shot examples; clinical-decision caveats (FDA SaMD may apply).
- **PCI DSS v4.x (payments)**: card numbers (PAN) and CVV must never enter prompts, logs, or memory; keep model out of cardholder-data scope.
- **GLBA / SOX / DORA / MiFID (finance)**: model-risk management, auditability, third-party ICT risk (DORA, EU), suitability and disclosure for advice.
- **FERPA / education**: student records.
- **SOC 2 / ISO 27001**: security controls evidence; logging, access control, change management.

## Other AI-specific guidance
- UK ICO guidance on AI and data protection; Singapore Model AI Governance Framework; Canada AIDA status (not enacted at last check)
- Anthropic/OpenAI/Google provider usage policies and deployment guidance: confirm the prompt does not violate the model provider's acceptable-use terms

When the user asks for "others", pick the 1–3 that fit the domain and state why, rather than listing everything.
