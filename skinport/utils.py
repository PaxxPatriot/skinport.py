__all__ = ("market_hash_name",)

from .enums import Exterior


def market_hash_name(item_name: str, condition: Exterior):
    """
    Generates a market hash name from an item name and condition.
    :param item_name: The name of the item.
    :param condition: The condition of the item.
    :return: The market hash name.
    """
    return f"{item_name} ({condition})"