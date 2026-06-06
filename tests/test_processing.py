from src import processing
import pytest


@pytest.mark.parametrize(
    "list_to_filter, state, expected",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
    ],
)
def test_filter_by_state(list_to_filter: list, state: str, expected: str) -> None:
    assert processing.filter_by_state(list_to_filter, state) == expected
