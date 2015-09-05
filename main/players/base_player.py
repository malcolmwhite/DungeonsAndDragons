from main.utils.utils import generate_attribute
from main.utils.utils import simulate_chance
from main.managers.item_manager import ItemManager


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

    def __init__(self, name, item_manager=None, speed=None, hp=None, defense=None, atk=None):
        self.NAME = name
        self.item_manager = item_manager if item_manager is not None else ItemManager()
        self._SPEED = speed if speed is not None else generate_attribute(self._AVERAGE_SPEED, self._SPEED_SPREAD)
        self.HP = hp if hp is not None else generate_attribute(self._AVERAGE_HP, self._HP_SPREAD)
        self._DEF = defense if defense is not None else generate_attribute(self._AVERAGE_DEF, self._DEF_SPREAD)
        self._ATK = atk if atk is not None else generate_attribute(self._AVERAGE_ATK, self._ATK_SPREAD)

    def __str__(self):
        return ''.join([str(self.NAME), ' ', str(self.HP)])

    def initialize_conflict(self):
        pass

    def finalize_conflict(self):
        if self._SPOOK_ROUNDS_AHEAD > 0:
            self._decrement_spook()

    def get_conflict_priority(self):
        boost = self.item_manager.get_speed_boost()
        return self._SPEED + boost

    def get_effective_attack(self):
        if self.HP == 0:
            return 0

        boost = self.item_manager.get_atk_boost()
        penalty = self._get_attack_penalty()
        return self._ATK - penalty + boost

    def get_effective_defense(self):
        boost = self.item_manager.get_def_boost()
        penalty = self._get_def_penalty()
        return self._DEF - penalty + boost

    def is_active(self):
        return self.HP > 0

    def is_spooked(self):
        return self._SPOOK_PENALTY > 0

    def add_item(self, item):
        self.item_manager.add_item(item)

    def add_items(self, items):
        self.item_manager.add_items(items)

    def dump_all_items(self):
        return self.item_manager.dump_all_items()

    def receive_attack(self, attack_points):
        hp_loss = max(attack_points - self.get_effective_defense(), 1)
        hp_loss = min(self.HP, hp_loss)
        self.HP -= hp_loss
        return hp_loss

    def receive_spook(self, spook_rate, spook_power):
        spook_success = False
        if simulate_chance(spook_rate):
            self._initialize_spook(spook_power)
            spook_success = True
        return spook_success

    def get_spook_params(self):
        return self.item_manager.get_spook_params()

    def get_formatted_name(self):
        name = self.NAME
        if self.is_spooked():
            name += " (spooked)"
        return name

    def get_formatted_attack(self):
        return "ATK: " + str(self._ATK)

    def get_formatted_defense(self):
        return "DEF: " + str(self._DEF)

    def get_formatted_hp(self):
        return "HP: " + str(self.HP)

    def get_formatted_items(self):
        return self.item_manager.get_formatted_items()

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



