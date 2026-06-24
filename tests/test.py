import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.masks import get_mask_card_number, get_mask_account

card = "7000792289606361"
print(f"Карта: {card} -> {get_mask_card_number(card)}")

account = "73654108430135874305"
print(f"Счет: {account} -> {get_mask_account(account)}")