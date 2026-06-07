from datetime import date

from tea_kb.io.frontmatter_dates import update_updated_date_text


def test_update_updated_date_replaces_existing_value() -> None:
    text = """---
id: note:test:example
status: active
created: 2026-06-01
updated: 2026-06-02
---

# Example
"""

    updated = update_updated_date_text(text, date(2026, 6, 7))

    assert "created: 2026-06-01" in updated
    assert "updated: 2026-06-07" in updated
    assert updated.count("updated:") == 1


def test_update_updated_date_inserts_after_created_when_missing() -> None:
    text = """---
id: note:test:example
status: active
created: 2026-06-01
---

# Example
"""

    updated = update_updated_date_text(text, date(2026, 6, 7))

    assert "created: 2026-06-01\nupdated: 2026-06-07" in updated
