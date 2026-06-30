"""
Модуль с функциями форматирования данных.
"""

from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(account_data: str) -> str:
    """
    Маскирует данные карты или счета.

    Args:
        account_data: Строка с типом и номером (например, "Visa 1234567890123456")

    Returns:
        Строка с замаскированными данными
    """
    parts = account_data.split()
    if len(parts) < 2:
        return account_data
    card_type = " ".join(parts[:-1])
    number = parts[-1]
    if any(keyword in card_type.lower() for keyword in ["visa", "mastercard", "мир", "maestro", "платежная"]):
        masked_number = get_mask_card_number(number)
    else:
        masked_number = get_mask_account(number)
    return f"{card_type} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует строку с датой в формат ДД.ММ.ГГГГ.

    Args:
        date_string: Строка с датой в формате ISO (YYYY-MM-DDTHH:MM:SS)

    Returns:
        Дата в формате ДД.ММ.ГГГГ
    """
    date_part = date_string.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"
