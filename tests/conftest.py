import pytest


@pytest.fixture
def widget_mask_account_card_data() -> str:
    return "Maestro 1596837868705199"


@pytest.fixture
def widget_mask_account_card_data_2() -> str:
    return "Счет 64686473678894779589"


@pytest.fixture
def widget_get_date_data() -> str:
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def masks_get_mask_card_number_data() -> str:
    return "8990922113665229"


@pytest.fixture
def masks_get_mask_account_data() -> str:
    return "64686473678894779589"


@pytest.fixture
def processing_filter_by_state_data() -> tuple[list, str]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ], "EXECUTED"


@pytest.fixture
def processing_sort_by_date_data() -> tuple[list, bool]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ], True
