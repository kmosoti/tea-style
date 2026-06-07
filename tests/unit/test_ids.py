from tea_kb.domain.ids import concept_id_for, is_valid_id, slugify


def test_id_validation_accepts_type_prefixed_ids() -> None:
    assert is_valid_id("note:evidence:systems-should-tell-on-themselves")
    assert is_valid_id("concept:evidence")


def test_id_validation_rejects_uppercase_and_spaces() -> None:
    assert not is_valid_id("Note:Evidence:Bad")
    assert not is_valid_id("note:evidence:bad id")


def test_slugify_and_concept_id() -> None:
    assert slugify("State Exposure!") == "state-exposure"
    assert concept_id_for("State Exposure") == "concept:state-exposure"
