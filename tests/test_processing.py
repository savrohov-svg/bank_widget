"""Модуль с тестами для функций обработки транзакций."""

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state() -> None:
    """Тестирует функцию filter_by_state."""
    operations = [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-11T02:26:18.671407"},
        {"id": 2, "state": "PENDING", "date": "2024-03-10T02:26:18.671407"},
        {"id": 3, "state": "EXECUTED", "date": "2024-03-09T02:26:18.671407"},
        {"id": 4, "state": "CANCELED", "date": "2024-03-08T02:26:18.671407"},
    ]

    result = filter_by_state(operations)
    assert len(result) == 2
    assert all(op["state"] == "EXECUTED" for op in result)
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3

    result = filter_by_state(operations, "PENDING")
    assert len(result) == 1
    assert result[0]["id"] == 2

    result = filter_by_state(operations, "CANCELED")
    assert len(result) == 1
    assert result[0]["id"] == 4


def test_sort_by_date() -> None:
    """Тестирует функцию sort_by_date."""
    operations = [
        {"id": 1, "date": "2024-03-11T02:26:18.671407"},
        {"id": 2, "date": "2024-03-10T02:26:18.671407"},
        {"id": 3, "date": "2024-03-12T02:26:18.671407"},
        {"id": 4, "date": "2024-03-09T02:26:18.671407"},
    ]

    result = sort_by_date(operations)
    assert len(result) == 4
    assert result[0]["id"] == 3
    assert result[1]["id"] == 1
    assert result[2]["id"] == 2
    assert result[3]["id"] == 4

    result = sort_by_date(operations, descending=False)
    assert len(result) == 4
    assert result[0]["id"] == 4
    assert result[1]["id"] == 2
    assert result[2]["id"] == 1
    assert result[3]["id"] == 3
