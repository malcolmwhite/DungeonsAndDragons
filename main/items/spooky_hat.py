from main.items.base_item import BaseItem
from main.managers.item_manager import ItemManager


class SpookyHat(BaseItem):
    CATEGORY_NAME = ItemManager.HAT_CATEGORY_NAME

    _AVERAGE_SPOOK_RATE = 5
    _AVERAGE_SPOOK_POWER = 5

    _SPOOK_RATE_SPREAD = 2.5
    _SPOOK_POWER_SPREAD = 2.5

    PRIMARY_VALUE = BaseItem.SPOOK_RATE * BaseItem.SPOOK_POWER

    def __init__(self, attack=None, defense=None, speed=None, spook_rate=None, spook_power=None):
        BaseItem.__init__(self, attack, defense, speed, spook_rate, spook_power)

