import pytest

from src import generators


@pytest.fixture
def transactions() -> list[dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_filter_by_currency(transactions: list[dict]) -> None:
    assert list(generators.filter_by_currency(transactions)) == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]


@pytest.mark.parametrize(
    "transaction_list, currency, expected",
    [
        ([], None, []),
        ([], "RUB", []),
        ([], "USD", []),
    ],
)
def test_filter_by_currency_parameter(transaction_list: list[dict], currency: str, expected: str) -> None:
    assert list(generators.filter_by_currency(transaction_list, currency)) == expected


def test_transaction_descriptions(transactions: list[dict]) -> None:
    assert list(generators.transaction_descriptions(transactions)) == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.mark.parametrize(
    "transaction_list, expected",
    [
        ([], []),
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
            ],
            ["Перевод организации"],
        ),
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
            ["Перевод организации", "Перевод со счета на счет"],
        ),
    ],
)
def test_transaction_descriptions_parameter(transaction_list: list[dict], expected: str) -> None:
    assert list(generators.transaction_descriptions(transaction_list)) == expected


@pytest.fixture()
def card_numbers() -> tuple[int, int]:
    return 12, 14


def test_card_number_generator(card_numbers: tuple[int, int]) -> None:
    assert list(generators.card_number_generator(card_numbers[0], card_numbers[1])) == [
        "0000 0000 0000 0012",
        "0000 0000 0000 0013",
        "0000 0000 0000 0014",
    ]


def test_card_number_generator_equal_numbers() -> None:
    assert list(generators.card_number_generator(12, 12)) == [
        "0000 0000 0000 0012",
    ]


def test_card_number_generator_bad_example() -> None:
    with pytest.raises(OverflowError):
        list(generators.card_number_generator(14, 12))


def test_card_number_generator_bad_example_1() -> None:
    with pytest.raises(OverflowError):
        list(generators.card_number_generator(-1, 12))



def test_card_number_generator_bad_example_3() -> None:
    with pytest.raises(OverflowError):
        list(generators.card_number_generator(2, 99999999999999990))


@pytest.mark.parametrize(
    "start_number, end_number, expected",
    [
        (12, 12, ["0000 0000 0000 0012"]),
        (0, 0, ["0000 0000 0000 0000"]),
        (1234567898765432, 1234567898765432, ["1234 5678 9876 5432"]),
    ],
)
def test_card_number_generator_param(start_number: int, end_number: int, expected: list) -> None:
    assert list(generators.card_number_generator(start_number, end_number)) == expected
