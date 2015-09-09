from src.main.beans.items.base_item import BaseItem


class ItemManager(object):

    # Category names are used to validate item instances and to map them to their corresponding bags
    SWORD_CATEGORY_NAME = "SWORD"
    SHIELD_CATEGORY_NAME = "SHIELD"
    HAT_CATEGORY_NAME = "HAT"
    SHOE_CATEGORY_NAME = "SHOES"
    _CATEGORY_NAMES = {SWORD_CATEGORY_NAME, SHIELD_CATEGORY_NAME, HAT_CATEGORY_NAME, SHOE_CATEGORY_NAME}

    def __init__(self, items=None):
        self._SWORD_BAG = []
        self._SHIELD_BAG = []
        self._HAT_BAG = []
        self._SHOES_BAG = []
        if items:
            self.add_items(items)

    def get_atk_boost(self):
        boost = 0
        if self._SWORD_BAG:
            boost += self._SWORD_BAG[0].ATTACK_BOOST
        return boost

    def get_def_boost(self):
        boost = 0
        if self._SHIELD_BAG:
            boost += self._SHIELD_BAG[0].DEFENSE_BOOST
        return boost

    def get_speed_boost(self):
        boost = 0
        if self._SHOES_BAG:
            boost += self._SHOES_BAG[0].SPEED_BOOST
        return boost

    def get_spook_rate_and_power(self):
        rate = 0
        power = 0
        if self._HAT_BAG:
            hat = self._HAT_BAG[0]
            hat_rate, hat_power = hat.get_spook_rate_and_power()
            rate += hat_rate
            power += hat_power
        return rate, power

    def add_items(self, items):
        map(self.add_item, items)

    def add_item(self, item):
        self._validate_item(item)
        item_category = item.CATEGORY_NAME
        item_bag = self._get_bag_for_category(item_category)
        item_bag.append(item)
        item_bag.sort(key=lambda x: x.PRIMARY_VALUE, reverse=True)

    def dump_all_items(self):
        """
        Remove all items from their bags and return as list. Item manager is empty after this is called.
        :return: List of items previously contained by item manager
        """
        dumped_items = []
        for category in self._CATEGORY_NAMES:
            item_bag = self._get_bag_for_category(category)
            dumped_items.extend(item_bag)
            del item_bag[:]
        return dumped_items

    def get_sword(self):
        return self._get_active_item(self._SWORD_BAG)

    def get_shield(self):
        return self._get_active_item(self._SHIELD_BAG)

    def get_hat(self):
        return self._get_active_item(self._HAT_BAG)

    def get_shoes(self):
        return self._get_active_item(self._SHOES_BAG)

    def get_formatted_items(self):
        output = "Items: "
        prefix = ""
        regular_prefix = " " * 7
        first_item = True
        for category in self._CATEGORY_NAMES:
            item_bag = self._get_bag_for_category(category)
            for item in item_bag:
                line = prefix + item.get_formatted_name()
                output = output + line + "\n"
                if first_item:
                    prefix = regular_prefix
                    first_item = False
        return output[:-1]

    def _get_bag_for_category(self, category_name):
        bag_name = "_" + category_name + "_BAG"
        return getattr(self, bag_name)

    @staticmethod
    def _get_active_item(items):
        if items:
            return items[0]
        else:
            return None

    def _validate_item(self, item):
        assert issubclass(item.__class__, BaseItem)
        if item.CATEGORY_NAME not in self._CATEGORY_NAMES:
            raise Exception
