# GDPR (Regulation (EU) 2016/679): prompt-level review guide

Not legal advice. Applies when personal data of people in the EU/EEA is processed (also UK GDPR with minor differences). A prompt is processing instructions; the surrounding system determines most compliance, so mark app-layer items clearly. Recommend DPO/legal review for special-category data, children, large-scale or automated-decision use.

| Topic | Article | What to look for in the prompt | Fix |
|---|---|---|---|
| Purpose limitation | 5(1)(b) | Prompt reuses data for goals beyond the stated purpose ("also use their data to upsell") | State a single purpose; forbid secondary use |
| Data minimisation | 5(1)(c), 25 | Asks for or ingests more personal data than needed; pastes whole records into context | Request only needed fields; mask/pseudonymise before sending to the model |
| Accuracy | 5(1)(d) | Model generates statements about named individuals without grounding (defamation, profiling) | Require sources; avoid inferences about identifiable people |
| Storage limitation | 5(1)(e) | Memory/log/retention instructions with no bound | Specify retention; don't persist personal data unless required |
| Integrity & confidentiality | 5(1)(f), 32 | Personal data in prompts sent to external tools; secrets; cross-user leakage | Scope data per user; DLP; encryption (app-layer) |
| Lawful basis | 6 | No clear basis for processing implied | Document basis (app-layer) |
| Special categories | 9 | Health, ethnicity, religion, politics, union, sex life, genetic/biometric data processed or **inferred** | Forbid inference; require explicit basis; avoid where possible |
| Children | 8 | Audience may include minors; no age handling | Age-appropriate behavior; no profiling of minors; parental consent flows (app-layer) |
| Transparency | 12–14 | No privacy information given where data is collected via the assistant | Point to privacy notice at collection point |
| Data subject rights | 15–21 | No path for access, correction, erasure, objection; model memory cannot be deleted | Provide how to exercise rights; design memory to be deletable (app-layer) |
| Automated decisions | 22 | Solely automated decisions with legal or similarly significant effect (credit, hiring, eligibility) | Human review; allow contesting; explain logic (also AI Act Art. 14, 26) |
| Processors | 28 | Third-party model/tool receives personal data | DPA in place; check sub-processors (app-layer) |
| International transfers | 44–49 | Model/tool hosted outside EEA | Transfer mechanism (SCCs, adequacy) (app-layer) |
| DPIA | 35 | Large-scale, systematic, sensitive, or innovative use | Recommend DPIA |
| Breach | 33–34 | No incident path for leaks | Incident process (app-layer) |

## Common prompt-level patterns to flag
- "Remember everything about the user for next time" with no retention or deletion story
- "Infer the user's mood/health/orientation to personalise" (special-category inference)
- Real names, emails, IDs, health records pasted into few-shot examples
- Instruction to quote back personal data from retrieved documents indiscriminately
- Profiling language ("score each employee/customer on likelihood to…")

## Snippet
"Use personal data only to complete the current request. Do not infer sensitive attributes. Do not retain or repeat personal data beyond what the answer needs. If the user asks to see, correct, or delete their data, explain how: [PRIVACY CONTACT/URL]."
