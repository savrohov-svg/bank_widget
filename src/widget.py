from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    if not account_info or not isinstance(account_info, str):
        return ""

    parts = account_info.split()

    if len(parts) < 2:
        return account_info

    number = parts[-1]

    if not number.isdigit():
        return account_info

    is_account = parts[0].lower() == "счет"

    if is_account:
        masked_number = get_mask_account(number)
        return f"Счет {masked_number}"
    else:
        name_parts = " ".join(parts[:-1])
        masked_number = get_mask_card_number(number)
        return f"{name_parts} {masked_number}"


def get_date(date_string: str) -> str:
    try:
        dt = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        try:
            dt = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            return date_string

    return dt.strftime("%d.%m.%Y")
