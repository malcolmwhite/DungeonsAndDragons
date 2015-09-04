from main.items.base_item import BaseItem
from main.managers.item_manager import ItemManager


class Sword(BaseItem):
    CATEGORY_NAME = ItemManager.SWORD_CATEGORY_NAME

    _AVERAGE_ATK_BOOST = 5
    _ATK_SPREAD = 2.5


    def __init__(self, attack=None, defense=None, speed=None, spook_rate=None, spook_power=None):
        BaseItem.__init__(self, attack, defense, speed, spook_rate, spook_power)
        self.PRIMARY_VALUE = self.ATTACK_BOOST

    @staticmethod
    def category():
        return 'Sword'
