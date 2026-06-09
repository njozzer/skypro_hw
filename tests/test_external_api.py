from unittest.mock import patch

from src import external_api


def test_transaction_convert_currency() -> None:
    with patch("requests.get") as mock_get:
        test_data = {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        }
        mock_get.return_value.json.return_value["success"] = True
        assert external_api.transaction_convert_currency(test_data) != 0.0
