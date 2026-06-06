import pytest


@pytest.fixture
def widget_mask_account_card_data() -> str:
    return "Maestro 1596837868705199"


@pytest.fixture
def widget_mask_account_card_data_2() -> str:
    return "Счет 64686473678894779589"


@pytest.fixture
def masks_get_mask_card_number_data() -> str:
    return "8990922113665229"


@pytest.fixture
def masks_get_mask_account_data() -> str:
    return "64686473678894779589"
