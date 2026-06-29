from src.widget import mask_account_card, get_date


def test_mask_account_card() -> None:
    """Тестирует функцию mask_account_card."""
    test_cases = [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ]

    for input_str, expected in test_cases:
        result = mask_account_card(input_str)
        assert result == expected, f"Failed: {input_str} -> {result}"
    print("All mask_account_card tests passed!")


def test_get_date() -> None:
    """Тестирует функцию get_date."""
    test_cases = [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11T02:26:18", "11.03.2024"),
    ]

    for input_str, expected in test_cases:
        result = get_date(input_str)
        assert result == expected, f"Failed: {input_str} -> {result}"
    print("All get_date tests passed!")


if __name__ == "__main__":
    test_mask_account_card()
    test_get_date()
    print("\n All tests passed successfully!")
