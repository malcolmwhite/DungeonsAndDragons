from src.main.utils.utils import generate_attribute

from src.main.utils.utils import raise_


class BaseItem(object):

    # Name used to discern where item should be stored in item manager.
    # Implementations of BaseItem should select a category name from ItemManager
    CATEGORY_NAME = lambda: raise_(NotImplementedError("CATEGORY_NAME is not implemented."))

    # Average values of core attributes.
    # These values may be overridden by inheriting classes to customize the type of item
    _AVERAGE_ATK_BOOST = 0
    _AVERAGE_DEF_BOOST = 0
    _AVERAGE_SPEED_BOOST = 0
    _AVERAGE_SPOOK_RATE = 0
    _AVERAGE_SPOOK_POWER = 0

    # Spread values indicate the standard deviation from the attribute average when randomly generated.
    # Values of zero indicate that the average value should be used.
    # These values may be overridden by inheriting classes to customize the type of item
    _ATK_SPREAD = 0
    _DEF_SPREAD = 0
    _SPEED_SPREAD = 0
    _SPOOK_RATE_SPREAD = 0
    _SPOOK_POWER_SPREAD = 0

    def __init__(self, attack=None, defense=None, speed=None, spook_rate=None, spook_power=None):
        if spook_power is not None and spook_power < 0:
            raise ValueError("spook_power must be greater than zero. Specified value was " + spook_power)
        self.ATTACK_BOOST = attack if attack is not None else generate_attribute(self._AVERAGE_ATK_BOOST,
                                                                                 self._ATK_SPREAD)
        self.DEFENSE_BOOST = defense if defense is not None else generate_attribute(self._AVERAGE_DEF_BOOST,
                                                                                    self._DEF_SPREAD)
        self.SPEED_BOOST = speed if speed is not None else generate_attribute(self._AVERAGE_SPEED_BOOST,
                                                                              self._SPEED_SPREAD)
        self.SPOOK_RATE = spook_rate if spook_rate is not None else generate_attribute(self._AVERAGE_SPOOK_RATE,
                                                                                       self._SPOOK_RATE_SPREAD)
        self.SPOOK_POWER = spook_power if spook_power is not None else generate_attribute(self._AVERAGE_SPOOK_POWER,
                                                                                          self._SPOOK_POWER_SPREAD)

        # Primary value is used by implementations of base item to indicate to item manager how the items are to
        # be prioritized. For example, a sword's primary value is attack and a shield's primary value is defense.
        # Swords will be ranked by their attack points and shields will be ranked by their defiense points.
        self.PRIMARY_VALUE = lambda: raise_(NotImplementedError("PRIMARY_VALUE is not implemented."))

    def get_spook_rate_and_power(self):
        return self.SPOOK_RATE, self.SPOOK_POWER

    def get_formatted_name(self):
        raise NotImplementedError("get_formatted_name is not implemented.")

    @staticmethod
    def _get_value_with_sign_prefix(value):
        prefix = "+" if float(value) > 0 else ""
        value = str(value)
        return prefix + value

    def __str__(self):
        return ''.join([self.CATEGORY_NAME, ' ', str(self.PRIMARY_VALUE)])

