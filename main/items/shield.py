from main.items.base_item import BaseItem
from main.managers.item_manager import ItemManager


class Shield(BaseItem):
    CATEGORY_NAME = ItemManager.SHIELD_CATEGORY_NAME

    _AVERAGE_DEF_BOOST = 5
    _DEF_SPREAD = 2.5

    PRIMARY_VALUE = BaseItem.DEFENSE_BOOST

    def __init__(self, attack=None, defense=None, speed=None, spook_rate=None, spook_power=None):
        BaseItem.__init__(self, attack, defense, speed, spook_rate, spook_power)

