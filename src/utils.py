import json
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def json_read_from_file(filename: str) -> list[dict]:
    """
    Считывает json файл
    :param filename: получает название файла
    :return: возвращает словари
    """
    logger.info(f"Вызвана json_read_from_file с файлом {filename}")
    try:
        if filename is None:
            logger.error(f"!Ожидалась строка, получен {type(filename).__name__}")
            return []
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info(f"Успешно считано из файла {filename}")
            return [item for item in data]
    except Exception as e:
        logger.error(f"Непредвиденная ошибка в json_read_from_file: {e}", exc_info=True)
    return []
