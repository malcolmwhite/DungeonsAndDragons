from src.main.managers.items.item_manager import ItemManager


class HardCodedAliceItemManager(ItemManager):
    def __init__(self, items):
        ItemManager.__init__(self, items)
        self.first_run = True

    def get_spook_rate_and_power(self):
        power = 0
        if self._HAT_BAG:
            hat = self._HAT_BAG[0]
            hat_rate, hat_power = hat.get_spook_rate_and_power()
            power += hat_power
        if self.first_run:
            rate = 100
            self.first_run = False
        else:
            rate = 0
        return rate, power