from main.beans.items.base_item import BaseItem


class ItemManager(object):
    SWORD_CATEGORY_NAME = "_SWORDS"
    SHIELD_CATEGORY_NAME = "_SHIELDS"
    HAT_CATEGORY_NAME = "_HATS"
    SHOE_CATEGORY_NAME = "_SHOES"
    _CATEGORY_NAMES = {SWORD_CATEGORY_NAME, SHIELD_CATEGORY_NAME, HAT_CATEGORY_NAME, SHOE_CATEGORY_NAME}

    def __init__(self, items=None):
        self._SWORDS = []
        self._SHIELDS = []
        self._HATS = []
        self._SHOES = []
        if items:
            self.add_items(items)

    def get_atk_boost(self):
        boost = 0
        if self._SWORDS:
            boost += self._SWORDS[0].ATTACK_BOOST
        return boost

    def get_def_boost(self):
        boost = 0
        if self._SHIELDS:
            boost += self._SHIELDS[0].DEFENSE_BOOST
        return boost

    def get_speed_boost(self):
        boost = 0
        if self._SHOES:
            boost += self._SHOES[0].SPEED_BOOST
        return boost

    def get_spook_params(self):
        rate = 0
        power = 0
        if self._HATS:
            hat = self._HATS[0]
            hat_rate, hat_power = hat.get_spook_rate_and_power()
            rate += hat_rate
            power += hat_power
        return rate, power

    def add_items(self, items):
        map(self.add_item, items)

    def add_item(self, item):
        self._validate_item(item)
        item_category = item.CATEGORY_NAME
        item_list = getattr(self, item_category)
        item_list.append(item)
        item_list.sort(key=lambda x: x.PRIMARY_VALUE, reverse=True)

    def dump_all_items(self):
        dumped_items = []
        for category in self._CATEGORY_NAMES:
            items = getattr(self, category)
            dumped_items.extend(items)
            del items[:]
        return dumped_items

    def get_sword(self):
        return self._get_active_item(self._SWORDS)

    def get_shield(self):
        return self._get_active_item(self._SHIELDS)

    def get_hat(self):
        return self._get_active_item(self._HATS)

    def get_shoes(self):
        return self._get_active_item(self._SHOES)

    def get_formatted_items(self):
        output = "Items: "
        prefix = ""
        regular_prefix = " " * 7
        first_item = True
        for category in self._CATEGORY_NAMES:
            items = getattr(self, category)
            for item in items:
                line = prefix + item.get_formatted_name()
                output = output + line + "\n"
                if first_item:
                    prefix = regular_prefix
                    first_item = False
        return output[:-1]


    @staticmethod
    def _add_item_and_sort(item, items):
        items.append(item)
        items.sort()

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
