__all__ = ("market_hash_name",)

from .enums import Exterior


def market_hash_name(item_name: str, exterior: Exterior):
    """
    Generates a market hash name from an item name and exterior.
    :param item_name: The name of the item.
    :param exterior: The exterior of the item.
    :return: The market hash name.
    """
    return f"{item_name} ({exterior})"
