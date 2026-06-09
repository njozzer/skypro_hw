import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """
    Функция get_mask_card_number получает номер карты,
     и возвращает замаскированный номер.
    """
    logger.info(f"Вызвана get_mask_card_number с номером карты {card_number}")
    try:
        if not isinstance(card_number, str):
            logger.error(f"!Ожидалась строка, получен {type(card_number).__name__}")
            raise TypeError
        if not len(card_number) == 16:
            logger.error("Ожидалось 16 цифр в номере карты")
            raise ValueError
        masked_number = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.info(f"Успешно замаскирован номер карты: {masked_number}")
        return masked_number
    except Exception as e:
        logger.error(f"Непредвиденная ошибка в get_mask_card_number: {e}", exc_info=True)
        raise e


def get_mask_account(account: str) -> str:
    """
    Функция get_mask_account получает номер аккаунта,
     и возвращает замаскированный номер.
    """
    logger.info(f"Вызвана get_mask_account с аккаунтом {account}")
    try:
        if not isinstance(account, str):
            logger.error(f"!Ожидалась строка, получен {type(account).__name__}")
            raise TypeError
        masked_account = f"**{account[-4:]}"
        logger.info(f"Успешно замаскирован аккаунт: {masked_account}")
        return masked_account
    except Exception as e:
        logger.error(f"Непредвиденная ошибка в get_mask_account: {e}", exc_info=True)
        raise e
