from main.items.base_item import BaseItem
from main.managers.item_manager import ItemManager


class Shoes(BaseItem):

    CATEGORY_NAME = ItemManager.SHOE_CATEGORY_NAME

    _AVERAGE_SPEED_BOOST = 5
    _SPEED_SPREAD = 2.5

    PRIMARY_VALUE = BaseItem.SPEED_BOOST

    def __init__(self, attack=None, defense=None, speed=None, spook_rate=None, spook_power=None):
        BaseItem.__init__(self, attack, defense, speed, spook_rate, spook_power)

