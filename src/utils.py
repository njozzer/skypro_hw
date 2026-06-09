import json
import logging
from typing import Any

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


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
