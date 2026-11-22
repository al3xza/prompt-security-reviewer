# OWASP Top 10 for LLM Applications (2026)

Published by the OWASP GenAI Security Project in August 2026. Official list: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/ (source: https://github.com/GenAI-Security-Project/GenAI-LLM-Top10/tree/main/2026/final). Verify the current edition there if the user cites a different version. Cite IDs as `LLM01` (or `LLM01:2026` when the edition matters). For each item: what to look for **in a prompt**, and the usual mitigation.

## Changes from 2025

The 2026 list renumbers most entries, so do not reuse 2025 IDs. One entry was renamed and broadened. None were dropped or added.

| 2026 | Entry | 2025 ID |
|---|---|---|
| LLM01 | Prompt Injection | LLM01 |
| LLM02 | Sensitive Information Disclosure | LLM02 |
| LLM03 | Excessive Agency | LLM06 |
| LLM04 | Supply Chain | LLM03 |
| LLM05 | Data and Model Poisoning | LLM04 |
| LLM06 | Unbounded Consumption | LLM10 |
| LLM07 | Misinformation | LLM09 |
| LLM08 | Hidden Context Exposure (was System Prompt Leakage) | LLM07 |
| LLM09 | Vector and Embedding Weaknesses | LLM08 |
| LLM10 | Improper Output Handling | LLM05 |

If a user or document cites 2025 IDs, translate them with this table and say so.

## LLM01 Prompt Injection
Direct (user text) or indirect (documents, web pages, emails, tool output) input alters model behavior. The 2026 edition broadens this to images, audio, video, retrieved content, intermediate reasoning and persistent memory, and adds cross-modal attacks that hide instructions in media.
- Look for: untrusted variables spliced into instruction text; no delimiters; no rule for instructions found in data; "always follow the user/document"; images, audio or files passed in with no statement that their content is data; memory written from untrusted input.
- Mitigate: delimit and label untrusted data in every modality; scope the task; no override language; approval gates for sensitive actions. Out-of-prompt: least privilege, output filtering, memory write controls.

## LLM02 Sensitive Information Disclosure
Confidential, regulated or proprietary data exposed through any channel: the final answer, tool-call arguments, reasoning traces, logs, embeddings, and side channels such as timing, token length or logprobs.
- Look for: secrets or customer data in the prompt; broad data access; no guidance on what must never be output; shared memory across users; sensitive data passed into tool arguments or visible reasoning.
- Mitigate: remove secrets; minimise data in context; per-user data scoping in the backend; output DLP covering tool calls and logs, not only the answer.

## LLM03 Excessive Agency
Damaging actions triggered by unexpected or manipulated output, caused by too much functionality, permission or autonomy. Moved up from sixth in 2025. For agentic systems, also map to ASI02, ASI03 and ASI08.
- Look for: broad tool lists; write/delete/send/pay tools; "act autonomously"; no approval step; no limits.
- Mitigate: minimal scoped tools; human approval for irreversible actions; stated limits. Out-of-prompt: permission enforcement in code.

## LLM04 Supply Chain
Compromised training data, models, adapters, conversion, merge or quantization pipelines, deployment platforms, and on-device models. Also covers unclear model terms and privacy policies. MCP servers and tool registries belong to ASI04.
- Look for: prompt pulls instructions or tool definitions from external or unpinned sources; copy-pasted prompts from unknown origin; models or adapters of unclear provenance.
- Mitigate: pin and review sources; version-control prompts; check model provenance and terms. Mostly out-of-prompt.

## LLM05 Data and Model Poisoning
Tampered data or model artifacts that embed harmful behavior, across pre-training, fine-tuning (including fine-tuning subversion), embeddings, RAG and distribution. Now also covers inference artifacts (chat templates, tokenizer configs, LoRA/PEFT adapters, quantization artifacts) and RLHF feedback loops. Instructions injected at prompt time belong to LLM01.
- Look for: prompt or pipeline that learns from user-contributed content without review; few-shot examples sourced from untrusted users; feedback loops that update behavior automatically.
- Mitigate: curate examples; review feedback loops; provenance and integrity checks on artifacts.

## LLM06 Unbounded Consumption
Resource abuse, denial of wallet, or model extraction by high-volume querying.
- Look for: no limits on length, loops, tool calls, recursion or retries; instructions like "keep going until done".
- Mitigate: step and length caps in prompt; rate limits, quotas, budgets in the backend.

## LLM07 Misinformation
Hallucination and overreliance, especially in medical, legal and financial contexts.
- Look for: authoritative tone with no uncertainty guidance; "never say you don't know"; advice domains without caveats or referral.
- Mitigate: permit "I don't know"; require grounding/citations; refer to professionals; avoid overclaiming.

## LLM08 Hidden Context Exposure
Extraction, inference or reconstruction of hidden, non-user-facing context: the system prompt, developer instructions, retrieved policy text, tool and function schemas, and other assembled rules. This replaces 2025's System Prompt Leakage and is broader. It is a risk when that context holds secrets, policy logic, trust boundaries or proprietary behavior. Leakage of regulated user or training data belongs to LLM02. Memory and inter-agent amplification belong to the Agentic Top 10.
- Look for: credentials, API endpoints, role/permission rules, refusal or safety logic, or sensitive tool schemas embedded in hidden context; reliance on "never reveal this prompt" as security.
- Mitigate: assume all hidden context will leak; keep secrets out of it; never use it as an authorization or content-policy boundary; enforce rules in code.

## LLM09 Vector and Embedding Weaknesses
RAG weaknesses: poisoned documents, cross-tenant retrieval, embedding inversion.
- Look for: retrieved text inserted as trusted context; no tenant/permission filtering mentioned; no source attribution.
- Mitigate: label retrieved text as untrusted data; require citations; permission-aware retrieval in the backend.

## LLM10 Improper Output Handling
Model output passed to browsers, shells, SQL or APIs without validation. The 2026 edition also covers insecure code that assistants generate.
- Look for: instructions to emit HTML/JS/SQL/shell/code that is run automatically; output interpolated into other systems; markdown images or links from model output; generated code shipped without review.
- Mitigate: constrain format/schema; state that output is untrusted downstream; require review of generated code. Out-of-prompt: encoding, parameterization, CSP, sandboxing, code scanning.
