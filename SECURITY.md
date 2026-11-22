# Security policy

## Reporting a vulnerability

Please do not open a public issue for security problems.

Report them privately through GitHub: go to the repository's **Security** tab and choose **Report a vulnerability**. Include what you found, how to reproduce it, and the impact you expect.

You should get a first reply within 7 days. Once a fix is ready, it will be released and the report credited unless you ask otherwise.

## What counts

In scope:

- Instructions in `skills/prompt-security-reviewer/SKILL.md` or its `references/` that could lead Claude to follow instructions hidden in the prompt under review, write attack payloads, or reproduce secrets it was shown, including pre-scan matches it should have redacted
- Guidance in the skill's `references/` that is wrong in a way that would make a reviewed prompt less safe

Out of scope:

- False positives or negatives in the pre-scan rules (open a normal issue)
- The underlying model's own behavior, which should be reported to its provider

## Supported versions

Only the latest commit on `main` is supported.
