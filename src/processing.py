def filter_by_state(list_to_filter: list, state: str = "EXECUTED") -> list:
    """
    Функция filter_by_state, которая принимает список словарей и
    опционально значение для ключа state (по умолчанию
    'EXECUTED').
    Функция возвращает новый список словарей, содержащий
    только те словари, у которых ключ state соответсвует
    значению переменной state.
    """
    filtered_list = [item for item in list_to_filter if item["state"] == state]
    return filtered_list


def sort_by_date(list_to_sort: list, descending: bool = True) -> list:
    """
    Функция sort_by_date, которая принимает список словарей и
    опционально значение, задающее порядок сортировки (по умолчанию
    убывание).
    Функция возвращает отсортированный список по дате.
    """
    sorted_list = sorted(list_to_sort, key=lambda x: x["date"], reverse=descending)
    return sorted_list


if __name__ == "__main__":
    data = [
        {'id': 41428829, 'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED',
         'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED',
         'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED',
         'date': '2018-10-14T08:21:33.419441'}]
    print(filter_by_state(data))
    print(sort_by_date(data))
