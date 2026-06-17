import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Возвращает список транзакций, в описании которых найдена указанная подстрока. Поиск регистронезависим
    :param data: список транзакций
    :param search: подстрока по которой искать
    :return:
    """
    if not search:
        return data
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [item for item in data if pattern.search(str(item.get("description", "")))]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """

    :param data:  Список транзакций
    :param categories: Список категорий
    :return:
    """
    counts = Counter(op.get("description") for op in data)
    return {category: counts[category] for category in categories}
