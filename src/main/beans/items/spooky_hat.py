from src.main.beans.items.base_item import BaseItem
from src.main.managers.items.item_manager import ItemManager


class SpookyHat(BaseItem):
    CATEGORY_NAME = ItemManager.HAT_CATEGORY_NAME

    _AVERAGE_SPOOK_RATE = 25
    _AVERAGE_SPOOK_POWER = 2

    _SPOOK_RATE_SPREAD = 20
    _SPOOK_POWER_SPREAD = 1

    def __init__(self, attack=None, defense=None, speed=None, spook_rate=None, spook_power=None):
        BaseItem.__init__(self, attack, defense, speed, spook_rate, spook_power)

        self.PRIMARY_VALUE = self.SPOOK_RATE * self.SPOOK_POWER

    def get_formatted_name(self):
        return "Hat (" + str(self.SPOOK_RATE) + "%, -" + str(self.SPOOK_POWER) + ")"