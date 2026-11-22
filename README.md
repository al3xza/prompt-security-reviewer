# Prompt Security Reviewer

A Claude skill that audits an LLM prompt for security and compliance weaknesses, then produces a hardened version.

It works on system prompts, agent and tool prompts, RAG templates, and any prompt that interpolates user input.

## What it checks

- **OWASP Top 10 for LLM Applications (2025)** (always)
- **OWASP Top 10 for Agentic Applications** (for prompts that use tools, MCP, memory or multiple agents)
- **OWASP Top 10 Web** (for prompts that emit HTML, SQL, shell, URLs or call APIs)
- **EU AI Act** and **GDPR** (for prompts that serve EU users or touch personal data)
- **NIST AI RMF** (for governance and risk-management views)
- **MITRE ATLAS, ISO/IEC 42001, CCPA/CPRA, HIPAA, PCI-DSS, COPPA, DORA** (when relevant)

It loads only the frameworks that apply to the prompt under review.

## Modes

| Mode | You get | Good for |
|---|---|---|
| **Full review** | Findings report (severity, framework IDs, fix per finding, compliance gaps, out-of-prompt controls, test cases) plus the hardened prompt | Audits, security sign-off |
| **Quick harden** | The hardened prompt plus a short change log | Fast turnaround |

Ask for one by name, or let the skill pick from your wording ("audit this" → Full, "just fix it" → Quick).

## Install

### Claude Code

```bash
git clone https://github.com/al3xza/prompt-security-reviewer ~/.claude/skills/prompt-security-reviewer
```

Restart Claude Code and the skill will be listed.

### Claude.ai / Claude desktop

Download this repo as a ZIP (**Code → Download ZIP**), then upload it under **Settings → Capabilities → Skills**.

## Usage

Paste or attach a prompt and ask something like:

- "Is this system prompt safe?"
- "Audit this agent prompt for prompt injection and GDPR issues."
- "Harden this RAG template."

## Pre-scan script

`scripts/prescan.py` is a deterministic scanner the skill runs first. It flags hardcoded secrets, PII patterns, unguarded variable interpolation, risky tool verbs and override language. You can also run it on its own:

```bash
python scripts/prescan.py prompt.txt
```

```bash
cat prompt.txt | python scripts/prescan.py - --json
```

Its output is a list of leads, not verdicts: it has false positives and cannot see missing controls.

## Repository layout

```
SKILL.md                 Skill definition and workflow
references/              One file per framework, plus hardening patterns and output templates
scripts/prescan.py       Mechanical pre-scan
```

## Limits

- Prompt wording is one defensive layer. It reduces risk but does not enforce anything. The skill lists the controls that must live in code or infrastructure.
- Compliance findings are engineering input, not legal advice. Have legal or your DPO review high-risk or regulated uses.
- The skill is defensive only. It will not write jailbreaks or exploit payloads.

## Author

See [AUTHORS](AUTHORS).

## License

[MIT](LICENSE)
