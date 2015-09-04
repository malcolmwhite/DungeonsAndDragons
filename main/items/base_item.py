from main.utils.utils import generate_attribute

from main.utils.utils import raise_


class BaseItem(object):
    CATEGORY_NAME = lambda: raise_(NotImplementedError("CATEGORY_NAME is not implemented."))

    _AVERAGE_ATK_BOOST = 0
    _AVERAGE_DEF_BOOST = 0
    _AVERAGE_SPEED_BOOST = 0
    _AVERAGE_SPOOK_RATE = 0
    _AVERAGE_SPOOK_POWER = 0

    _ATK_SPREAD = 0
    _DEF_SPREAD = 0
    _SPEED_SPREAD = 0
    _SPOOK_RATE_SPREAD = 0
    _SPOOK_POWER_SPREAD = 0

    ATTACK_BOOST = 0
    DEFENSE_BOOST = 0
    SPEED_BOOST = 0
    SPOOK_RATE = 0
    SPOOK_POWER = 0

    PRIMARY_VALUE = lambda: raise_(NotImplementedError("PRIMARY_VALUE is not implemented."))

    def __init__(self, attack=None, defense=None, speed=None, spook_rate=None, spook_power=None):
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

    def get_spook_rate_and_power(self):
        return self.SPOOK_RATE, self.SPOOK_POWER

    def __str__(self):
        print ''.join([self.CATEGORY_NAME, ' ', str(self.PRIMARY_VALUE)])

