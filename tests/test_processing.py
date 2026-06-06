import pytest

from src import processing


@pytest.mark.parametrize(
    "list_to_filter, state, expected",
    [],
)
def test_filter_by_state(list_to_filter: list, state: str, expected: list) -> None:
    assert processing.filter_by_state(list_to_filter, state) == expected


@pytest.mark.parametrize(
    "list_to_sort, descending, expected",
    [],
)
def test_sort_by_date(list_to_sort: list, descending: bool, expected: list) -> None:
    assert processing.sort_by_date(list_to_sort, descending) == expected
