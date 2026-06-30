"""
Модуль с функциями обработки транзакций.
"""

from typing import Any, Dict, List


def filter_by_state(operations: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует список операций по статусу state."""
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список операций по дате."""
    return sorted(operations, key=lambda x: x.get("date", ""), reverse=descending)
