from unittest.mock import mock_open, patch

from src import utils


def test_json_read_from_file() -> None:
    data = """{"operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}}"""
    with patch("builtins.open", mock_open(read_data=data)) as mock_openfile:
        assert utils.json_read_from_file("operations.json") == {
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}
        }

        assert mock_openfile.call_count == 1


def test_json_read_from_file_None() -> None:
    data = """{"operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}}"""
    with patch("builtins.open", mock_open(read_data=data)) as mock_openfile:
        assert utils.json_read_from_file(None) == []  # type: ignore[arg-type]

        assert mock_openfile.call_count == 0


def test_json_read_from_file_Bad_JSON() -> None:

    with patch("builtins.open", mock_open(read_data=None)) as mock_openfile:
        assert utils.json_read_from_file("test_2.json") == []

        assert mock_openfile.call_count == 1


def test_json_read_from_file_File_Not_Found() -> None:

    assert utils.json_read_from_file("test_2.json") == []
