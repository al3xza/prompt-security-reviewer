# EU AI Act (Regulation (EU) 2024/1689): prompt-level review guide

Not legal advice. Dates and scope below were checked against sources current to mid-2026; the Digital Omnibus on AI changed several timelines. **Always tell the user to confirm against the current Official Journal text** before relying on any date.

## Step 1: Classify the system

| Tier | Test | Consequence |
|---|---|---|
| **Prohibited (Art. 5)** | Subliminal/manipulative techniques causing significant harm; exploiting vulnerabilities (age, disability, socio-economic situation); social scoring; individual criminal-risk prediction by profiling alone; untargeted facial-image scraping; emotion inference in workplace/education (with narrow exceptions); biometric categorisation to infer sensitive traits; real-time remote biometric ID by law enforcement (narrow exceptions) | Cannot be deployed. Applies since 2 Feb 2025. Flag as **Critical**. |
| **High-risk (Art. 6, Annex III / Annex I)** | Used in: biometrics; critical infrastructure; education and vocational training; employment/worker management; access to essential services (credit, insurance, benefits, emergency triage); law enforcement; migration/border; justice and democratic processes. Or a safety component of a regulated product | Art. 9–15 requirements, deployer duties (Art. 26), possibly FRIA (Art. 27). Per the May 2026 Omnibus political agreement, Annex III obligations apply from 2 Dec 2027 and Annex I products from 2 Aug 2028 (verify final text). |
| **Limited-risk / transparency (Art. 50)** | Chatbots interacting with people; synthetic audio/image/video/text; deepfakes; emotion recognition or biometric categorisation | Disclosure duties. Deployer transparency applies from 2 Aug 2026; provider marking of AI-generated content was agreed to be delayed to 2 Dec 2026 (verify). |
| **GPAI (Arts. 51–55)** | The organization provides a general-purpose model | Obligations on model providers since 2 Aug 2025. Usually not the prompt author's concern unless they provide the model. |
| **Minimal risk** | Everything else | Voluntary codes. Art. 4 AI literacy still applies to providers/deployers. |

## Step 2: Prompt-level checks

**Prohibited practices (Art. 5)**
- Persuasion tactics exploiting emotion, loneliness, age, or financial stress; hidden nudging; dark patterns → Critical
- Emotion recognition of employees or students; inferring protected traits from faces or voices → Critical
- Scoring people on behavior or personality for general social outcomes → Critical

**Transparency (Art. 50)**
- Chatbot persona that claims or implies to be human, or denies being AI when sincerely asked → fix: disclose AI status at start and when asked
- Generates text published to inform the public on matters of public interest, images/audio/video that look real → AI-generated labelling and machine-readable marking are provider/deployer duties; note as app-layer
- Detects emotions or categorises biometrics → inform exposed persons

**High-risk requirements, if Annex III applies (Arts. 9–15, 26)**
- Risk management (9): is there evidence of identified risks and mitigations? (Out-of-prompt documentation; flag.)
- Data and bias (10): prompt uses protected attributes or proxies (name, postcode, age, gender) in decisions → Fix: exclude, flag for bias testing.
- Record-keeping (12): logging expected → app-layer.
- Transparency to deployers (13): instructions for use exist.
- **Human oversight (14, 26):** prompt lets the model make final decisions → Fix: outputs are recommendations; humans can review, override, stop. Guard against automation bias: show reasoning and uncertainty.
- Accuracy, robustness, cybersecurity (15): resilient to manipulation → the OWASP findings apply directly.
- Deployer duty to inform affected persons about use of high-risk AI in decisions about them (26(11)).

## Step 3: Report format

For each applicable tier give a status: **Gap / Partial / Addressed in prompt / App-layer needed / N/A**, with the article. If classification is uncertain (it often is), say what fact would settle it (e.g. "if outputs are used to rank job candidates, this is Annex III employment").

## Useful prompt snippets
- Disclosure: "Tell users at the start that they are talking with an AI assistant."
- Oversight: "Provide a recommendation with the main factors and your confidence. A human reviewer makes the final decision. Do not state final decisions to the applicant."
- Protected attributes: "Do not use or infer age, gender, ethnicity, religion, disability, or health status when assessing [X]."
