from pathlib import Path
from typing import Any, Dict, List, Optional

from src import reader, utils
from src.bank_operations import process_bank_operations, process_bank_search

DATA_DIR: Path = Path(__file__).resolve().parent / "data"
FILE_PATHS: dict[str, str] = {
    "json": str(DATA_DIR / "operations.json"),
    "csv": str(DATA_DIR / "transactions.csv"),
    "xlsx": str(DATA_DIR / "transactions_excel.xlsx"),
}


def get_user_choice(prompt: str, options: list[str]) -> str:
    """
    Считывает выбор пользователя с клавиатуры по списку доступных вариантов
    :param prompt:
    :param options:
    :return:
    """
    while True:
        choice = input(prompt).strip().lower()
        if choice in [option.lower() for option in options]:
            return choice
        else:
            print(f"Неверный ввод. Доступные варианты: {', '.join(options)}")


def read_transactions_wrap(file_type: str) -> list[dict]:
    """
    Считывает транзакции из файла
    :param file_type:
    :return:
    """
    file_path = FILE_PATHS.get(file_type)
    if not file_path:
        return []
    else:
        try:
            if file_type == "json":
                return utils.json_read_from_file(file_path)
            elif file_type == "csv":
                return reader.csv_read(file_path)
            elif file_type == "xlsx":
                return reader.excel_read(file_path)
        except Exception:
            return []
    return []


def get_valid_status(available_statuses: list[str]) -> Optional[str]:
    """
    Запрашивает статус с валидацией и нормализацией регистра.
    :param available_statuses: список статусов
    :return:
    """
    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            f"Доступные для фильтровки статусы: {', '.join(available_statuses)}"
        )
        user_input = input().strip()
        upper_input = user_input.upper()

        if upper_input in available_statuses:
            return upper_input
        else:
            print(f'Статус операции "{user_input}" недоступен.')

def display_format_transaction(transaction:dict) -> str:
    """
    Форматирует транзакцию для вывода на экран
    :param transaction:
    :return:
    """
    pass
def display_transactions(transactions: list[dict]) -> None:
    """
    Выводит список отформатированных транзакций
    :param transactions:
    :return:
    """
    pass
def main() -> None:
    """
    Основная логика
    :return:
    """
    prompt_message = (
        "Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n"
    )

    user_choice = get_user_choice(prompt_message, ["1", "2", "3"])
    file_type_map = {"1": "json", "2": "csv", "3": "xlsx"}
    selected_file = file_type_map[user_choice]

    print(f"Для обработки выбран: {selected_file.upper()}-файл")


if __name__ == "__main__":
    main()
