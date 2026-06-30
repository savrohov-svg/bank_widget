"""
Модуль с функциями маскировки номеров карт и счетов.
"""


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты: видны первые 6 и последние 4 цифры."""
    if len(card_number) != 16:
        return card_number
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета: видны только последние 4 цифры."""
    if len(account_number) < 4:
        return account_number
    return f"**{account_number[-4:]}"
