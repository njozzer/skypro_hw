from unittest.mock import patch

import requests

from src import external_api


def test_transaction_convert_currency() -> None:
    with patch("requests.get") as mock_get:
        test_data = {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "EUR", "code": "EUR"}},
        }
        temp = {
            "success": True,
            "timestamp": 1780994527,
            "base": "EUR",
            "date": "2026-06-09",
            "rates": {"RUB": 82.788208},
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = temp

        assert external_api.transaction_convert_currency(test_data) == 680632.49


def test_transaction_convert_currency_RUB() -> None:

    test_data = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "руб.", "code": "RUB"}},
    }
    assert external_api.transaction_convert_currency(test_data) == 8221.37


def test_transaction_convert_currency_Bad_Format() -> None:
    with patch("requests.get"):
        test_data = {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "822f1.37", "currency": {"name": "руб.", "code": "RUB"}},
        }

        assert external_api.transaction_convert_currency(test_data) == 0.0


def test_transaction_convert_currency_Bad_Response() -> None:
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 404
        test_data = {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "EUR", "code": "EUR"}},
        }
        assert external_api.transaction_convert_currency(test_data) == 0.0


def test_transaction_convert_currency_Response_None_Rates() -> None:
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 404
        test_data = {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "822f1.37", "currency": {"name": "руб.", "code": "RUB"}},
        }
        assert external_api.transaction_convert_currency(test_data) == 0.0


def test_transaction_convert_currency_Response_Bad_Currency() -> None:
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 404
        test_data = {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8123", "currency": {"name": "BTC", "code": "BTC"}},
        }
        assert external_api.transaction_convert_currency(test_data) == 0.0


def test_transaction_convert_currency_Response_Bad_Response() -> None:
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 404
        test_data = {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8123", "currency": {"name": "BTC", "code": "BTC"}},
        }
        assert external_api.transaction_convert_currency(test_data) == 0.0


def test_transaction_convert_currency_Response_None_Rate() -> None:
    with patch("requests.get") as mock_get:
        test_data = {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "EUR", "code": "EUR"}},
        }
        temp = {"success": True, "timestamp": 1780994527, "base": "EUR", "date": "2026-06-09"}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = temp

        assert external_api.transaction_convert_currency(test_data) == 0.0


def test_transaction_convert_currency_exception() -> None:
    with patch("requests.get") as mock_get:
        test_data = {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "EUR", "code": "EUR"}},
        }

        mock_get.side_effect = requests.exceptions.RequestException

        try:
            external_api.transaction_convert_currency(test_data)
        except requests.RequestException:
            print("Error")


def test_transaction_convert_currency_json_exception_ValueError() -> None:
    with patch("requests.get") as mock_get:
        test_data = {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "EUR", "code": "EUR"}},
        }
        mock_get.side_effect = ValueError
        try:
            external_api.transaction_convert_currency(test_data)
        except ValueError:
            print("Error")


def test_transaction_convert_currency_json_exception_KeyError() -> None:
    with patch("requests.get") as mock_get:
        test_data = {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "EUR", "code": "EUR"}},
        }
        mock_get.side_effect = ValueError
        try:
            external_api.transaction_convert_currency(test_data)
        except KeyError:
            print("Error")
