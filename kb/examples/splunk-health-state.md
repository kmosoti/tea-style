---
id: example:observability:splunk-health-state
title: Splunk Health State
type: example
domain: observability
status: active
created: 2026-06-07
updated: 2026-06-07
summary: >
  Health should be reported as layered evidence, not a single unsupported label.
concepts:
  - observability
  - evidence
  - explicit-state
edges:
  exemplifies:
    - note:observability:operators-should-not-hallucinate-system-state
origin:
  author: human
  review: manual
---

# Splunk Health State

## Example
```text
process: splunkd running
api: REST endpoint responds
cluster: peer is searchable
workflow: host can safely receive work
```

## Point
Health is layered. A live process is not the same as a ready system.
