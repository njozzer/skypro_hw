import json
from typing import Any


def json_read_from_file(filename: str) -> Any:
    """
    Считывает json файл
    :param filename: получает название файла
    :return: возвращает словари
    """
    if filename is None:
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("Error: The file does not exist.")
        return []
    except json.JSONDecodeError:
        print("Error: The file contains invalid JSON syntax.")
        return []
