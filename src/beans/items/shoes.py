from src.beans.items.base_item import BaseItem
from src.managers.items.item_manager import ItemManager


class Shoes(BaseItem):
    CATEGORY_NAME = ItemManager.SHOE_CATEGORY_NAME

    _AVERAGE_SPEED_BOOST = 5
    _SPEED_SPREAD = 2.5

    def __init__(self, attack=None, defense=None, speed=None, spook_rate=None, spook_power=None):
        BaseItem.__init__(self, attack, defense, speed, spook_rate, spook_power)

        self.PRIMARY_VALUE = self.SPEED_BOOST

    def get_formatted_name(self):
        return "Shoes (" + self._get_value_with_sign_prefix(self.SPEED_BOOST) + ")"