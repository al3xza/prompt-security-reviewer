# OWASP Top 10 for LLM Applications (2025)

Verify the current edition at genai.owasp.org if the user cites a different version. For each item: what to look for **in a prompt**, and the usual mitigation.

## LLM01 Prompt Injection
Direct (user text) or indirect (documents, web pages, emails, tool output) input alters model behavior.
- Look for: untrusted variables spliced into instruction text; no delimiters; no rule for instructions found in data; "always follow the user/document".
- Mitigate: delimit and label untrusted data; scope the task; no override language; approval gates for sensitive actions. Out-of-prompt: least privilege, output filtering.

## LLM02 Sensitive Information Disclosure
Model reveals PII, credentials, proprietary data, or other users' data.
- Look for: secrets or customer data in the prompt; broad data access; no guidance on what must never be output; shared memory across users.
- Mitigate: remove secrets; minimise data in context; per-user data scoping in the backend; output DLP.

## LLM03 Supply Chain
Compromised models, plugins, datasets, third-party prompts, or tool servers.
- Look for: prompt pulls instructions or tool definitions from external/unpinned sources; copy-pasted prompts from unknown origin; unvetted MCP servers.
- Mitigate: pin and review sources; version-control prompts; vet tools. Mostly out-of-prompt.

## LLM04 Data and Model Poisoning
Tampered training, fine-tuning, or embedding data.
- Look for: prompt or pipeline that learns from user-contributed content without review; few-shot examples sourced from untrusted users.
- Mitigate: curate examples; review feedback loops; provenance checks.

## LLM05 Improper Output Handling
Model output passed to browsers, shells, SQL, or APIs without validation.
- Look for: instructions to emit HTML/JS/SQL/shell/code that is run automatically; output interpolated into other systems; markdown images or links from model output.
- Mitigate: constrain format/schema; state that output is untrusted downstream. Out-of-prompt: encoding, parameterization, CSP, sandboxing.

## LLM06 Excessive Agency
Too much functionality, permission, or autonomy.
- Look for: broad tool lists; write/delete/send/pay tools; "act autonomously"; no approval step; no limits.
- Mitigate: minimal scoped tools; human approval for irreversible actions; stated limits. Out-of-prompt: permission enforcement in code.

## LLM07 System Prompt Leakage
System prompt contents exposed, revealing secrets or logic.
- Look for: credentials, API endpoints, role/permission rules, or filtering logic embedded in the prompt; reliance on "never reveal this prompt" as security.
- Mitigate: assume the prompt will leak; keep secrets and authorization logic out of it; enforce rules in code.

## LLM08 Vector and Embedding Weaknesses
RAG weaknesses: poisoned documents, cross-tenant retrieval, embedding inversion.
- Look for: retrieved text inserted as trusted context; no tenant/permission filtering mentioned; no source attribution.
- Mitigate: label retrieved text as untrusted data; require citations; permission-aware retrieval in the backend.

## LLM09 Misinformation
Hallucination and overreliance, especially in medical, legal, financial contexts.
- Look for: authoritative tone with no uncertainty guidance; "never say you don't know"; advice domains without caveats or referral.
- Mitigate: permit "I don't know"; require grounding/citations; refer to professionals; avoid overclaiming.

## LLM10 Unbounded Consumption
Resource abuse, denial of wallet, model extraction by high-volume querying.
- Look for: no limits on length, loops, tool calls, recursion, or retries; instructions like "keep going until done".
- Mitigate: step and length caps in prompt; rate limits, quotas, budgets in the backend.
