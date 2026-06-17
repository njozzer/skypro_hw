from typing import Any, Generator


def filter_by_currency(transaction_list: list[dict], currency: str = "USD") -> Generator[Any, Any, None]:
    """

    :param transaction_list: список транзакций
    :param currency: Опциональный параметр валюты
    :return: Генератор отфильтрованных по валюте транзакций
    """
    for transaction in transaction_list:
        if transaction.get("operationAmount").get("currency").get("code") == currency:  # type: ignore[union-attr]
            yield transaction


def transaction_descriptions(transaction_list: list) -> Generator[str, Any, None]:
    """

    :param transaction_list: список транзакций
    :return: Генератор описаний транзакций
    """
    for transaction in transaction_list:
        yield transaction.get("description")


def card_number_generator(start_number: int, end_number: int) -> Generator[str, Any, None]:
    """

    :param start_number: Начальное число для генерации номеров карт
    :param end_number: Конечное число для генерации номеров карт
    :return: Генератор номеров карт
    """
    if start_number > end_number:
        raise OverflowError
    if start_number < 0:
        raise OverflowError
    if end_number > 9999999999999999:
        raise OverflowError
    for card in range(start_number, end_number + 1):
        card_number = [str(digit) for digit in str(card)]
        result = "".join(card_number)
        if len(card_number) < 16:
            result = (16 - len(card_number)) * "0" + result
            yield f"{result[0:4]} {result[4:8]} {result[8:12]} {result[12:]}"
        elif len(card_number) == 16:
            yield f"{result[0:4]} {result[4:8]} {result[8:12]} {result[12:]}"
