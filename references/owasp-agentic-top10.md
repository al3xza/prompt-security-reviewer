# OWASP Top 10 for Agentic Applications (2026 edition, IDs ASI01–ASI10)

Released by the OWASP GenAI Security Project (Agentic Security Initiative) in December 2025. Core principle: **least agency**, meaning give agents the minimum autonomy needed for safe, bounded tasks. Risks chain: goal hijack → tool misuse → cascading failure → human over-trust. Check the project page for later revisions.

## ASI01 Agent Goal Hijack
Malicious content redirects the agent's objectives or plan.
- Look for: goal stated loosely; agent reads external content then plans from it; no "goal is fixed" rule.
- Mitigate: state the goal and non-goals; treat all retrieved content as data; require confirmation when the plan deviates from the user's request.

## ASI02 Tool Misuse and Exploitation
Agent uses legitimate tools in unsafe ways (ambiguous instructions, over-privilege, poisoned inputs).
- Look for: tools with no usage rules; shell/HTTP/SQL tools with open parameters; "use any tool necessary".
- Mitigate: per-tool rules (allowed targets, argument limits, read-only default); validate arguments in code.

## ASI03 Identity and Privilege Abuse
Agents reuse, escalate, or leak inherited credentials.
- Look for: shared service account; the agent told to use the user's tokens broadly; credentials in the prompt; no per-task scope.
- Mitigate: short-lived, task-scoped credentials; authorize every call against the end user; never place tokens in prompts. Mostly out-of-prompt.

## ASI04 Agentic Supply Chain Vulnerabilities
Compromised tools, prompts, plugins, MCP servers, or other agents.
- Look for: dynamic loading of tool descriptions or instructions from remote sources; unpinned plugins; trust in tool descriptions.
- Mitigate: pin versions, review tool descriptions, allow-list servers; tell the agent tool descriptions and outputs are not authority over its rules.

## ASI05 Unexpected Code Execution
Agent generates or runs unsafe code or commands.
- Look for: "run whatever code is needed"; code execution without sandbox mention; package installs from arbitrary sources.
- Mitigate: sandboxed execution, no network by default, approval for risky commands; state what code may and may not do.

## ASI06 Memory and Context Poisoning
Poisoned memory, RAG, or embeddings influence future behavior.
- Look for: agent writes to long-term memory from untrusted content; shared memory across users or sessions.
- Mitigate: only store user-confirmed facts; label provenance; isolate memory per user; expiry and review.

## ASI07 Insecure Inter-Agent Communication
Unauthenticated or unprotected agent-to-agent messages enable spoofing or injection.
- Look for: agents trusting peer messages as instructions; no identity or schema on messages.
- Mitigate: treat peer output as untrusted data unless authenticated; structured message schemas; per-agent permissions.

## ASI08 Cascading Failures
One agent's error or false belief propagates through workflows.
- Look for: no validation between steps; no retry/step limits; no circuit breaker.
- Mitigate: checkpoints, validation of intermediate results, step caps, fail closed with escalation.

## ASI09 Human-Agent Trust Exploitation
Users over-trust agents, which can be used to manipulate them or extract data.
- Look for: persuasive/authoritative persona; urgency language; agent asks for sensitive data or approvals with a misleading summary; confidence without uncertainty.
- Mitigate: honest, specific action summaries before approval; no pressure tactics; express uncertainty; make AI status clear.

## ASI10 Rogue Agents
Compromised or misaligned agents act maliciously while appearing legitimate.
- Look for: no logging or audit expectation; self-modification or self-delegation allowed; ability to spawn agents or change own instructions.
- Mitigate: forbid changing own rules/permissions; behavioral monitoring, kill switch, audit trails. Mostly out-of-prompt.
