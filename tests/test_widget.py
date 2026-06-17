import pytest

from src import widget


@pytest.mark.parametrize(
    "card, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(card: str, expected: str) -> None:
    assert widget.mask_account_card(card) == expected


def test_mask_account_card_none() -> None:
    with pytest.raises(ValueError):
        widget.mask_account_card(None)  # type: ignore[arg-type]


def test_mask_account_card_non_str() -> None:
    with pytest.raises(TypeError):
        widget.mask_account_card(123)  # type: ignore[arg-type]


def test_mask_account_card_bad_card() -> None:
    with pytest.raises(ValueError):
        widget.mask_account_card(" 1596837868705199")


def test_mask_account_card_bad_card_2() -> None:
    with pytest.raises(ValueError):
        widget.mask_account_card("Maestro")


def test_mask_account_card_bad_card_3() -> None:
    with pytest.raises(ValueError):
        widget.mask_account_card("M 1596837868705199")


def test_mask_account_card_bad_account() -> None:
    with pytest.raises(ValueError):
        widget.mask_account_card("Сч3ет 353830334323744478935560")


def test_mask_account_card_bad_account_2() -> None:
    with pytest.raises(ValueError):
        widget.mask_account_card("С 353830334744478935")


def test_mask_account_card_bad_account_3() -> None:
    with pytest.raises(ValueError):
        widget.mask_account_card("Счет 3538303347133344478935560")


def test_mask_account_card_fixture(widget_mask_account_card_data: str) -> None:
    assert widget.mask_account_card(widget_mask_account_card_data) == "Maestro 1596 83** **** 5199"


def test_mask_account_card_fixture_2(widget_mask_account_card_data_2: str) -> None:
    assert widget.mask_account_card(widget_mask_account_card_data_2) == "Счет **9589"


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11T02", "11.03.2024"),
        ("2026-06-06 21:10:00", "06.06.2026"),
    ],
)
def test_get_date(date: str, expected: str) -> None:
    assert widget.get_date(date) == expected


def test_get_date_bad_date() -> None:
    with pytest.raises(TypeError):
        widget.get_date(12)  # type: ignore[arg-type]


def test_get_date_bad_date_2() -> None:
    with pytest.raises(ValueError):
        widget.get_date("06/06/2026")


def test_get_date_bad_date_3() -> None:
    with pytest.raises(ValueError):
        widget.get_date("06.06.2026")


def test_get_date_fixture(widget_get_date_data: str) -> None:
    assert widget.get_date(widget_get_date_data) == "11.03.2024"
