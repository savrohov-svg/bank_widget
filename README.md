# Bank Widget

## Описание
Проект для работы с банковскими виджетами и маскировкой данных.
Проект для обучения и познания новых знаний.

## Установка

## Функции обработки данных

### filter_by_state(operations, state='EXECUTED')
Фильтрует список операций по статусу.

**Пример:**
```python
from src.processing import filter_by_state

data = [
    {'id': 1, 'state': 'EXECUTED'},
    {'id': 2, 'state': 'CANCELED'}
]
result = filter_by_state(data, 'CANCELED')
print(result)  # [{'id': 2, 'state': 'CANCELED'}]

1. Клонируйте репозиторий:
```bash
git clone https://github.com/savrohov-svg/bank_widget.git
cd bank_widget