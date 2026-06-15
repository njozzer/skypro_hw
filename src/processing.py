def filter_by_state(list_to_filter: list, state: str = "EXECUTED") -> list:
    """
    Функция filter_by_state, которая принимает список словарей и
    опционально значение для ключа state (по умолчанию
    'EXECUTED').
    Функция возвращает новый список словарей, содержащий
    только те словари, у которых ключ state соответсвует
    значению переменной state.
    """

    filtered_list = [item for item in list_to_filter if item.get("state") == state]
    return filtered_list


def sort_by_date(list_to_sort: list, descending: bool = True) -> list:
    """
    Функция sort_by_date, которая принимает список словарей и
    опционально значение, задающее порядок сортировки (по умолчанию
    убывание).
    Функция возвращает отсортированный список по дате.
    """

    return sorted(list_to_sort, key=lambda x: x.get("date"), reverse=descending)


def filter_by_currency(list_to_filter: list[dict], currency: str = "RUB") -> list[dict]:
    """
    Фильтрация по транзакциям с рублями
    :param currency:
    :param list_to_filter:
    :return:
    """
    filtered_list = [item for item in list_to_filter if item.get("currency_code") == currency]
    return filtered_list
