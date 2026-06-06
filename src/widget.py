from datetime import datetime

from src import masks


def mask_account_card(card: str) -> str:
    """
    Функция mask_account_card, которая принимает аккаунт, или
    номер карты, и возвращает ее замаскированное значение.
    """
    if not card:
        raise ValueError("!Ошибка: пустая строка")
    if not isinstance(card, str):
        raise TypeError(f"!Ожидалась строка, получен {type(card).__name__}")
    letter_arr: list[str] = []
    digit_arr: list[str] = []
    for char in card:
        if char.isalpha() or char.isspace():
            letter_arr.append(char)
        elif char.isdigit():
            digit_arr.append(char)
    letter_str = "".join(letter_arr).strip()
    if not letter_str:
        raise ValueError("!Ошибка: не найдено букв")
    digit_str = "".join(digit_arr)
    if not digit_str:
        raise ValueError("!Ошибка: не найдено цифр")
    if letter_str == "Счет":
        if len(digit_str) != 20:
            raise ValueError(f"!Ошибка: номер счета должен содержать " f"20 цифр (получено {len(digit_str)})")
        return f"{letter_str} {masks.get_mask_account(digit_str)}"
    else:
        if len(digit_str) != 16:
            raise ValueError(f"!Ошибка: номер карты содержит " f"{len(digit_str)} цифр (ожидается 16)")
        if len(letter_str) < 2:
            raise ValueError("!Ошибка: слишком короткое имя карты")
        return f"{letter_str} {masks.get_mask_card_number(digit_str)}"


def get_date(date: str) -> str:
    """
    Функция get_date, которая принимает дату в формате
    iso строки.
    Функция возвращает дату в формате дд.мм.гггг
    (д - день, м - месяц, г - год).
    """
    if not isinstance(date, str):
        raise TypeError(f"!Ожидалась строка, получен {type(date).__name__}")
    if date == "":
        return datetime.today().strftime("%d.%m.%Y")
    try:
        curr_date = datetime.fromisoformat(date)
    except ValueError:
        pass
    finally:
        return datetime.strptime(date,"%m/%d/%Y").strftime("%d.%m.%Y")



if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
