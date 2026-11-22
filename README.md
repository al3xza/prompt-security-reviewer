# Prompt Security Reviewer

A Claude skill that audits an LLM prompt for security and compliance weaknesses, then produces a hardened version.

It works on system prompts, agent and tool prompts, RAG templates, and any prompt that interpolates user input.

## What it checks

- **OWASP Top 10 for LLM Applications (2026)** (always)
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

This repo is a Claude plugin that contains one skill.

### Claude.ai, Claude desktop and Cowork

Open the Claude directory, search for **Prompt Security Reviewer** and add it.

### Claude Code

```bash
npx skills add al3xza/prompt-security-reviewer -g -a claude-code
```

Or copy the skill folder by hand:

```bash
git clone https://github.com/al3xza/prompt-security-reviewer /tmp/prompt-security-reviewer
cp -R /tmp/prompt-security-reviewer/skills/prompt-security-reviewer ~/.claude/skills/
```

Restart Claude Code and the skill will be listed.

## Usage

Paste or attach a prompt and ask something like:

- "Is this system prompt safe?"
- "Audit this agent prompt for prompt injection and GDPR issues."
- "Harden this RAG template."

## Pre-scan

Before the main review, the skill runs a quick pass from `references/prescan-checklist.md`. It flags hardcoded secrets, PII patterns, unguarded variable interpolation, risky tool verbs and override language. Its matches are leads, not verdicts: they include false positives, and the checklist cannot see missing controls.

The plugin is instructions only. It runs no code, sends no data anywhere and fetches nothing.

## Repository layout

```
.claude-plugin/plugin.json                      Plugin manifest
.claude-plugin/icon.png                         Directory icon
skills/prompt-security-reviewer/SKILL.md        Skill definition and workflow
skills/prompt-security-reviewer/references/     One file per framework, plus the pre-scan checklist, hardening patterns and output templates
```

## Security

To report a vulnerability, see [SECURITY.md](SECURITY.md). Please don't open a public issue.

## Limits

- Prompt wording is one defensive layer. It reduces risk but does not enforce anything. The skill lists the controls that must live in code or infrastructure.
- Compliance findings are engineering input, not legal advice. Have legal or your DPO review high-risk or regulated uses.
- The skill is defensive only. It will not write jailbreaks or exploit payloads.

## Author

See [AUTHORS](AUTHORS.md).

## License

[MIT](LICENSE)
