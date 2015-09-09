from src.main.beans.items.base_item import BaseItem
from src.main.managers.items.item_manager import ItemManager


class Sword(BaseItem):
    CATEGORY_NAME = ItemManager.SWORD_CATEGORY_NAME

    _AVERAGE_ATK_BOOST = 5
    _ATK_SPREAD = 1

    def __init__(self, attack=None, defense=None, speed=None, spook_rate=None, spook_power=None):
        BaseItem.__init__(self, attack, defense, speed, spook_rate, spook_power)

        self.PRIMARY_VALUE = self.ATTACK_BOOST

    def get_formatted_name(self):
        return "Sword (" + self._get_value_with_sign_prefix(self.ATTACK_BOOST) + ")"
