from pathlib import Path
from typing import Optional

from src import filter_by_state, generators, get_date, mask_account_card, processing, reader, sort_by_date, utils
from src.bank_operations import process_bank_search

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


def format_amount(transaction: dict) -> str:
    amount_data = transaction.get("operationAmount")

    if isinstance(amount_data, dict):
        amount = amount_data.get("amount", "0")
        currency_data = amount_data.get("currency", {})
        currency = (
            currency_data.get("name", currency_data.get("code", "RUB"))
            if isinstance(currency_data, dict)
            else str(currency_data)
        )
    else:
        amount = transaction.get("amount", "0")
        currency = transaction.get("currency_code", "RUB")

    return f"{amount} {currency}"


def display_format_transaction(transaction: dict) -> str:
    """
    Форматирует транзакцию для вывода на экран
    :param transaction: транзакция
    :return: строка
    """
    date = transaction.get("date", "")
    date_formatted = get_date(date) if date else "Неуказано"
    description = transaction.get("description")

    result = f"{date_formatted} {description}\n"

    list_account = []
    if transaction.get("from"):
        list_account.append(mask_account_card(str(transaction["from"])))
    if transaction.get("to"):
        list_account.append(mask_account_card(str(transaction["to"])))

    if list_account:
        result += " -> ".join(list_account) + "\n"
    result += f"Сумма: {format_amount(transaction)}"
    return result


def display_transactions(transactions: list[dict]) -> None:
    """
    Выводит список отформатированных транзакций
    :param transactions:
    :return:
    """
    print(f"\nВсего банковских операций в выборке: {len(transactions)}\n")
    for i, transaction in enumerate(transactions):
        print(display_format_transaction(transaction))
        if i + 1 < len(transactions):
            print("\n", end="")


def filter_transactions_by_currency(transactions: list[dict], file_type: str) -> list[dict]:

    if file_type == "json":
        filtered_transactions = [item for item in generators.filter_by_currency(transactions, currency="RUB")]
        return filtered_transactions
    else:
        filtered_transactions = processing.filter_by_currency(transactions, currency="RUB")
        return filtered_transactions


def main() -> None:
    """
    Основная логика
    :return:
    """
    # Выбор файла для чтения
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

    transactions = read_transactions_wrap(selected_file)
    if not transactions:
        print("Не удалось загрузить транзакции. Проверьте наличие и структуру файла.")
        return
    # Сортировка по статусу
    status = get_valid_status(["EXECUTED", "CANCELED", "PENDING"])
    if status is not None:
        print(f'Операции отфильтрованы по статусу "{status}"')
        transactions = filter_by_state(transactions, status)

    # Сортировка по дате
    if get_user_choice("\nОтсортировать операции по дате? Да/Нет: ", ["да", "нет"]) == "да":
        sort_order = get_user_choice(
            "Отсортировать по возрастанию или по убыванию? ", ["по возрастанию", "по убыванию"]
        )
        sort_order_bool = True if sort_order == "по убыванию" else False
        transactions = sort_by_date(transactions, descending=sort_order_bool)
    # Фильтрация по рублям
    if get_user_choice("\nВыводить только рублевые транзакции? Да/Нет: ", ["да", "нет"]) == "да":
        transactions = filter_transactions_by_currency(transactions, selected_file)

    # Фильтрация по ключевому слову
    if (
        get_user_choice("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет: ", ["да", "нет"])
        == "да"
    ):
        keyword = input("Введите слово, по которому нужно отфильтровать: ").strip()
        if keyword:
            transactions = process_bank_search(transactions, keyword)
    # Если пустой
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия")
        return
    print("\nРаспечатываю итоговый список транзакций...")
    display_transactions(transactions)


if __name__ == "__main__":
    main()
