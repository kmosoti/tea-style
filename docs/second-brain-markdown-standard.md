# Second Brain Markdown Standard

## Purpose
Define how `tea-style` should behave like a second brain while staying native to GitHub and Markdown.

## Core claim
The repository should be easy to browse, search, cross-link, and extend without requiring non-GitHub syntax, plugins, databases, or private note tooling.

## Definitions
- **Second-brain structure**: a knowledge system organized for retrieval, reuse, and connection.
- **Map of content**: an index page that explains a section and links related pages in a useful order.
- **Atomic page**: a page centered on one durable concept or closely related concept set.
- **Knowledge hook**: compact metadata in normal Markdown that helps humans and agents retrieve the page.
- **Backlink**: a normal Markdown link from one page to a related page.

## Rules / standards
- Use GitHub-native Markdown only.
- Use relative links to repository files.
- Prefer one durable concept per page.
- Keep README files and index pages as maps of content, not loose navigation dumps.
- Put related pages at the end of doctrine/reference pages.
- Use decision records for durable why, not for every small edit.
- Use compact examples near the domain they explain.
- Keep headings stable enough to be linked and searched.
- Prefer explicit file names over vague buckets like `notes.md` or `misc.md`.
- Avoid custom wiki-link syntax such as `[[page]]` because GitHub does not resolve it natively.

## Knowledge hooks
For substantial doctrine pages, include a short section near the top:

```md
## Knowledge hooks
- **Type**: doctrine
- **Domain**: automation
- **Concepts**: idempotency, state machine, evidence
- **Use when**: designing or reviewing a workflow that can mutate real systems
```

Hooks are not a database. They are visible retrieval cues.

## Map of content pages
README/index pages should answer:
- what belongs here
- what does not belong here
- which pages exist
- what order to read them in when learning the area

## Anti-patterns
- long unstructured notes dumps
- orphan pages with no related links
- plugin-only syntax that breaks in plain GitHub rendering
- duplicate pages that describe the same concept with different names
- hidden metadata that humans cannot review in rendered Markdown
- broad tags that do not improve retrieval

## Related pages
- [docs/repo-scope.md](repo-scope.md)
- [docs/page-template-standard.md](page-template-standard.md)
- [docs/repository-layout.md](repository-layout.md)
- [docs/decisions/README.md](decisions/README.md)
