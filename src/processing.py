def filter_by_state(operations: list, state: str = 'EXECUTED') -> list:
    """Фильтрует список операций по статусу state"""
    return [op for op in operations if op.get('state') == state]


def sort_by_date(operations: list, descending: bool = True) -> list:
    """Сортирует список операций по дате"""
    return sorted(operations, key=lambda x: x.get('date', ''), reverse=descending)
