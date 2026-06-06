def get_mask_card_number(card_number: str) -> str:
    """
    Функция get_mask_card_number получает номер карты,
     и возвращает замаскированный номер.
    """
    if not isinstance(card_number, str):
        raise TypeError(f"!Ожидалась строка, получен {type(card_number).__name__}")
    if not len(card_number) == 16:
        raise ValueError("Ожидалось 16 цифр в номере карты")
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """
    Функция get_mask_account получает номер аккаунта,
     и возвращает замаскированный номер.
    """
    if not isinstance(account, str):
        raise TypeError(f"!Ожидалась строка, получен {type(account).__name__}")
    return f"**{account[-4:]}"
