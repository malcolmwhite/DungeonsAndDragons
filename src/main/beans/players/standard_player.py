from src.main.utils.utils import generate_attribute
from src.main.utils.utils import simulate_chance
from src.main.utils.utils import get_trimmed_or_padded_string
from src.main.managers.items.item_manager import ItemManager


class StandardPlayer(object):
    # Average values of core attributes.
    # These values may be overridden by inheriting classes to customize the type of player
    _AVERAGE_SPEED = 0
    _AVERAGE_HP = 5
    _AVERAGE_DEF = 5
    _AVERAGE_ATK = 5

    # Spread values indicate the standard deviation from the attribute average when randomly generated.
    # Values of zero indicate that the average value should be used.
    # These values may be overridden by inheriting classes to customize the type of player
    _SPEED_SPREAD = 0
    _HP_SPREAD = 1
    _DEF_SPREAD = 1
    _ATK_SPREAD = 1

    def __init__(self, name, item_manager=None, speed=None, hp=None, defense=None, atk=None):
        self.NAME = name
        self.item_manager = item_manager if item_manager is not None else ItemManager()
        self._SPEED = int(speed) if speed is not None else generate_attribute(self._AVERAGE_SPEED, self._SPEED_SPREAD)
        self.HP = int(hp) if hp is not None else generate_attribute(self._AVERAGE_HP, self._HP_SPREAD)
        self._DEF = int(defense) if defense is not None else generate_attribute(self._AVERAGE_DEF, self._DEF_SPREAD)
        self._ATK = int(atk) if atk is not None else generate_attribute(self._AVERAGE_ATK, self._ATK_SPREAD)
        self._LOG_ATTRIBUTES = [self.get_formatted_name, self.get_formatted_attack, self.get_formatted_defense,
                                self.get_formatted_hp, self.get_formatted_items]

        self._SPOOK_ROUNDS_AHEAD = 0
        self._SPOOK_PENALTY = 0

    def __str__(self):
        return ''.join([str(self.NAME), ' ', str(self.HP)])

    # noinspection PyMethodMayBeStatic
    def initialize_confrontation(self):
        """
        Implementation left for inheriting classes.
        """
        pass

    def finalize_confrontation(self):
        """
        Update accounting for tallies that change per round, such as whether a player is spooked.
        """
        if self._SPOOK_ROUNDS_AHEAD > 0:
            self._decrement_spook()

    def get_round_priority(self):
        """
        Determine how early a player should act in a round.
        :return: number indicating priority. Higher values map to earlier position
        """
        boost = self.item_manager.get_speed_boost()
        return self._SPEED + boost

    def get_effective_attack(self):
        if not self.is_active():
            return 0

        boost = self.item_manager.get_atk_boost()
        penalty = self._get_attack_penalty()
        return self._ATK - penalty + boost

    def get_effective_defense(self):
        boost = self.item_manager.get_def_boost()
        penalty = self._get_def_penalty()
        return self._DEF - penalty + boost

    def is_active(self):
        """
        Indicates whether or not a player can take action.
        :return: True if player can take action
        """
        return self.HP > 0

    def is_spooked(self):
        """
        Indicates whether or not a player is spooked.
        :return: True if player is spooked
        """
        return self._SPOOK_PENALTY > 0

    def add_item(self, item):
        """
        Add an item to the player's item manager
        :param item: Item to be added
        """
        self.item_manager.add_item(item)

    def add_items(self, items):
        """
        Add a list of items to a player's item manager
        :param items: List of items
        """
        self.item_manager.add_items(items)

    def dump_all_items(self):
        """
        Remove all items from a player's item manager and return them.
        :return: List of items
        """
        return self.item_manager.dump_all_items()

    def receive_attack(self, attack_points):
        """
        Receive an attack with the given number of attack points, taking into account a player's items and whether or
        not they are spooked
        :param attack_points: attack points that the player is attacked with
        :return: amount of HP damage sustained in attack
        """
        hp_loss = max(attack_points - self.get_effective_defense(), 1)
        hp_loss = min(self.HP, hp_loss)
        self.HP -= hp_loss
        return hp_loss

    def receive_spook(self, spook_rate, spook_power):
        """
        Receive a spook attack with the given rate and power
        :param spook_rate: int percentage of spook success
        :param spook_power: reduction to player's attack and defense if spook succeeds
        :return: True if spook succeeds
        """
        spook_success = False
        if simulate_chance(spook_rate):
            self._initialize_spook(spook_power)
            spook_success = True
        return spook_success

    def get_spook_rate_and_power(self):
        """
        Get a player's spook rate and power
        :return: tuple (spook rate, spook power)
        """
        return self.item_manager.get_spook_rate_and_power()

    def get_formatted_name(self):
        """
        Get a player's name, formatted for printing
        :return: formatted name
        """
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

    def get_summary(self):
        summary = ""
        width = 25
        for attribute in self._LOG_ATTRIBUTES:
            attribute_lines = attribute().splitlines()
            for attribute_line in attribute_lines:
                attribute_line = get_trimmed_or_padded_string(attribute_line, width)
                summary += attribute_line + "\n"
        return summary

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



