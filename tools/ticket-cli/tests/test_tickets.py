import pytest

from ticket_cli.tickets import priority_rank


def test_urgent_ranks_above_high():
    assert priority_rank("urgent") > priority_rank("high")


def test_iscase_insensitive():
    assert priority_rank("LOW") == 1


def test_medium_is_between_low_and_high():
    assert priority_rank("low") < priority_rank("medium") < priority_rank("high")


def test_unkown_priority_raises():
    with pytest.raises(ValueError, match="Unkown priority"):
        priority_rank("banana")
