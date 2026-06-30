"""Модуль с тестами для функций маскировки."""

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    """Тестирует функцию get_mask_card_number."""
    card = "7000792289606361"
    assert get_mask_card_number(card) == "7000 79** **** 6361"
    card = "1234567890123456"
    assert get_mask_card_number(card) == "1234 56** **** 3456"
    card = "1596837868705199"
    assert get_mask_card_number(card) == "1596 83** **** 5199"
    card = "7158300734726758"
    assert get_mask_card_number(card) == "7158 30** **** 6758"


def test_get_mask_account() -> None:
    """Тестирует функцию get_mask_account."""
    account = "73654108430135874305"
    assert get_mask_account(account) == "**4305"
    account = "35383033474447895560"
    assert get_mask_account(account) == "**5560"
    account = "1234567890"
    assert get_mask_account(account) == "**7890"
