---
id: example:automation:safe-automation-script
title: Safe Automation Script
type: example
domain: automation
status: active
summary: >
  A safe automation script separates planning, validation, execution, and evidence.
concepts:
  - automation
  - evidence
  - mutation
edges:
  exemplifies:
    - note:mutation:mutation-should-be-atomic-visible-and-hard-to-misunderstand
    - note:evidence:systems-should-tell-on-themselves
origin:
  author: human
  review: manual
---

# Safe Automation Script

## Example
```text
load request
validate context
build plan
render dry-run
execute approved plan
collect evidence
write report
```

## Point
The script is safe because mutation is downstream from validation and planning.
