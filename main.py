from pathlib import Path
from typing import Any, Dict, List, Optional

from src.bank_operations import process_bank_operations, process_bank_search
from src.reader import csv_read, excel_read

DATA_DIR: Path = Path(__file__).resolve().parent / "data"
FILE_PATHS: Dict[str, str] = {
    "json": str(DATA_DIR / "operations.json"),
    "csv": str(DATA_DIR / "transactions.csv"),
    "xlsx": str(DATA_DIR / "transactions_excel.xlsx"),
}


def get_user_choice(prompt: str, options: List[str]) -> str:
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


def read_transactions(file_type:str) -> List[Dict]:
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
                pass
            elif file_type == "csv":
                pass
            elif file_type == "xlsx":
                pass
def get_valid_status(available_statuses: List[str]) -> Optional[str]:
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


if __name__ == "__main__":
    main()
