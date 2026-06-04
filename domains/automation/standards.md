# Automation Standards

## Review checks
- Is the control plane explicit?
- Is the execution flow diagnosable?
- Is rollback or recovery defined?
- Is source of truth obvious?
- Is the workflow maintainable by someone other than the author?
- Is there a dry-run or plan view before mutation?
- Are validation gates enforced before and after risky steps?
- Are retries safe for the command being retried?
- Is blast radius limited by policy?
- Is evidence captured in structured form?
