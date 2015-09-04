from main.utils.utils import generate_attribute
from main.utils.utils import simulate_chance


class BasePlayer(object):

    _SPOOK_ROUNDS_AHEAD = 0
    _SPOOK_PENALTY = 0

    _AVERAGE_SPEED = 0
    _AVERAGE_HP = 5
    _AVERAGE_DEF = 5
    _AVERAGE_ATK = 5

    _SPEED_SPREAD = 0
    _HP_SPREAD = 2.5
    _DEF_SPREAD = 2.5
    _ATK_SPREAD = 2.5

    def __init__(self, item_manager, speed=None, hp=None, defense=None, atk=None):
        self.item_manager = item_manager
        self._SPEED = speed if speed is not None else generate_attribute(self._AVERAGE_SPEED, self._SPEED_SPREAD)
        self.HP = hp if hp is not None else generate_attribute(self._AVERAGE_HP, self._HP_SPREAD)
        self._DEF = defense if defense is not None else generate_attribute(self._AVERAGE_DEF, self._DEF_SPREAD)
        self._ATK = atk if atk is not None else generate_attribute(self._AVERAGE_ATK, self._ATK_SPREAD)

    def initialize_conflict(self):
        pass

    def finalize_conflict(self):
        if self._SPOOK_ROUNDS_AHEAD > 0:
            self._decrement_spook()

    def confront_with_item(self, item):
        if simulate_chance(item.SPOOK_RATE):
            self._initialize_spook(item.SPOOK_POWER)

    def get_conflict_priority(self):
        boost = self.item_manager.get_speed_boost()
        return self._SPEED + boost

    def get_effective_attack(self):
        if self.HP == 0:
            return 0

        boost = self.item_manager.get_attack_boost()
        penalty = self._get_attack_penalty()
        return self._ATK - penalty + boost

    def get_effective_defense(self):
        boost = self.item_manager.get_hp_boost()
        penalty = self._get_def_penalty()
        return self._DEF - penalty + boost

    def _get_attack_penalty(self):
        return self._SPOOK_PENALTY

    def _get_def_penalty(self):
        return self._SPOOK_PENALTY

    def _initialize_spook(self, penalty):
        self._SPOOK_ROUNDS_AHEAD = 3
        self._SPOOK_PENALTY = penalty

    def _decrement_spook(self):
        self._SPOOK_ROUNDS_AHEAD = max(0, self._SPOOK_ROUNDS_AHEAD - 1)
        if self._SPOOK_ROUNDS_AHEAD == 0:
            self._SPOOK_PENALTY = 0



