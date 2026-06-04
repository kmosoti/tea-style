# Automation Anti-Patterns

## Reject
- hidden prerequisites
- manual tribal knowledge embedded in scripts
- non-idempotent workflows without clear warning
- duplicated configuration across systems
- automation that cannot explain its own failure
- dry-run implemented as scattered print statements
- unbounded parallel mutation
- retries without backoff, max attempts, or reconciliation
- workflow state stored only in human memory
- production mutation without change context or evidence
