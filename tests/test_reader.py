from unittest.mock import mock_open, patch

import pandas as pd

from src import reader


def test_csv_reader() -> None:
    data = (
        "id;state;date;amount;currency_name;currency_code;from;to;description"
        "\n650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации"  # noqa: E501
    )
    with patch("builtins.open", mock_open(read_data=data)) as mock_read:

        assert reader.csv_read("data/transactions.csv") == [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
        mock_read.assert_called_with("data/transactions.csv", encoding="utf-8")


def test_csv_writer_exception() -> None:
    data = (
        "id;state;date;amount;currency_name;currency_code;from;to;description"
        "\n650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации"  # noqa: E501
    )
    with patch("builtins.open", mock_open(read_data=data)) as mock_read:
        assert reader.csv_read(-1) == []  # type: ignore[arg-type]
        assert mock_read.call_count == 0


def test_excel_reader() -> None:

    with patch("pandas.read_excel") as mock_read:
        fake_df = pd.DataFrame(
            {
                "id": ["650703"],
                "state": ["EXECUTED"],
                "date": ["2023-09-05T11:30:32Z"],
                "amount": ["16210"],
                "currency_name": ["Sol"],
                "currency_code": ["PEN"],
                "from": ["Счет 58803664561298323391"],
                "to": ["Счет 39745660563456619397"],
                "description": ["Перевод организации"],
            }
        )
        mock_read.return_value = fake_df
        assert reader.excel_read("data/transactions.excel") == [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
        mock_read.assert_called_once_with("data/transactions.excel")


def test_excel_reader_exception() -> None:
    with patch("pandas.read_excel") as mock_read:
        fake_df = pd.DataFrame(
            {
                "id": ["650703"],
                "state": ["EXECUTED"],
                "date": ["2023-09-05T11:30:32Z"],
                "amount": ["16210"],
                "currency_name": ["Sol"],
                "currency_code": ["PEN"],
                "from": ["Счет 58803664561298323391"],
                "to": ["Счет 39745660563456619397"],
                "description": ["Перевод организации"],
            }
        )
        mock_read.return_value = fake_df
        assert reader.excel_read(-1) == []  # type: ignore[arg-type]
        assert mock_read.call_count == 0
