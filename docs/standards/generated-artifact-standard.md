---
id: standard:repo:generated-artifact-standard
title: Generated Artifact Standard
type: standard
domain: repo-wide
status: active
created: 2026-06-06
updated: 2026-06-07
summary: >
  Defines generated graph artifacts, stale checks, determinism, and review expectations.
concepts:
  - generated artifacts
  - determinism
  - reports
  - exports
edges:
  supports:
    - decision:repo:0003-ship-tea-kb-lifecycle-tooling
  depends_on:
    - standard:repo:graph-knowledge-base-standard
origin:
  author: human
  review: manual
---

# Generated Artifact Standard

## Purpose
Define which generated files exist and how they are reviewed.

## Core claim
Generated artifacts are derived from Markdown/frontmatter. They are committed when they are stable and useful for review.

## Generated artifacts
- `graph/generated/nodes.jsonl`
- `graph/generated/edges.jsonl`
- `graph/generated/chunks.jsonl`
- `graph/generated/concepts.jsonl`
- `graph/generated/timeline.jsonl`
- `graph/generated/index.html`
- `graph/generated/reports/health.md`
- `graph/generated/reports/orphan-notes.md`
- `graph/generated/reports/dense-links.md`
- `graph/generated/reports/duplicate-concepts.md`
- `graph/generated/reports/proposed-edges.md`
- `graph/generated/reports/timeline.md`
- `graph/generated/visualizations/overview.html`
- `graph/generated/visualizations/README.md`
- `graph/generated/visualizations/repo-system-light.svg`
- `graph/generated/visualizations/repo-system-dark.svg`
- `graph/generated/visualizations/research-support-light.svg`
- `graph/generated/visualizations/research-support-dark.svg`
- `graph/generated/visualizations/timeline-overview-light.svg`
- `graph/generated/visualizations/timeline-overview-dark.svg`
- `graph/generated/visualizations/concept-timeline-*-light.svg`
- `graph/generated/visualizations/concept-timeline-*-dark.svg`

## Rules / standards
- Generated artifacts must be deterministic.
- `tea-kb build --check` fails when generated artifacts are stale.
- Generated files are not canonical.
- Reports should be boring, useful, and reviewable.
- JSONL exports should be stable-sorted by ID or edge tuple.
- Visualization output should avoid avoidable randomness.
- Root README diagrams must be generated artifacts, not hand-maintained images.
- Timeline artifacts must be derived from `created` and `updated` frontmatter dates.
- `tea-kb build --check` must fail when stale files remain under `graph/generated`.
- Normal `tea-kb build` should prune unexpected files under `graph/generated` before writing current artifacts.
- CI uploads `graph/generated` as a workflow artifact for PR review.
- The Pages workflow publishes `graph/generated` from `main` as a static artifact browser when GitHub Pages is enabled.

## Related pages
- [graph-knowledge-base-standard.md](graph-knowledge-base-standard.md)
- [visualization-standard.md](visualization-standard.md)
