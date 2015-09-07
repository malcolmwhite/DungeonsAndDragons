from src.managers.players.base_player_manager import BasePlayerManager
from src.beans.players.base_player import BasePlayer
from src.beans.items.spooky_hat import SpookyHat
from src.beans.items.sword import Sword
from src.beans.items.shoes import Shoes
from src.beans.items.shield import Shield
from src.utils.utils import query_yes_no


class ManualPlayerManager(BasePlayerManager):
    _ACCEPTABLE_SWORD_NAMES = {"sword", "a sword", "swords"}
    _ACCEPTABLE_SHIELD_NAMES = {"shield", "a shield", "shields"}
    _ACCEPTABLE_SHOES_NAMES = {"shoe", "a shoe", "shoes"}
    _ACCEPTABLE_HAT_NAMES = {"hat", "a hat", "hats", "spooky hat", "a spooky hat"}

    def generate_players(self, num_players=None):
        while query_yes_no("Would you like to add a player?"):
            player = self._build_player_from_cmd()
            self.add_player(player)

    def _build_player_from_cmd(self):
        name = raw_input("Please enter the player's name.\n\t")
        atk = self._build_attribute_from_cmd("attack rating")
        defense = self._build_attribute_from_cmd("defense rating")
        hp = self._build_attribute_from_cmd("initial hp")
        speed = 0
        player = BasePlayer(name, None, speed, hp, defense, atk)
        item = self._build_item_from_cmd()
        player.add_item(item)
        return player

    def _build_attribute_from_cmd(self, attribute_name):
        value = raw_input("Please enter the player's {}. Leave blank to auto-generate.\n\t".format(attribute_name))
        if not len(value):
            value = None
        return value

    def _build_item_from_cmd(self):
        while 1:
            item_type = raw_input("Please specify item category. Options are: sword, shield, shoes, spooky hat.\n\t")
            item_type_lower = item_type.lower()
            if item_type_lower in self._ACCEPTABLE_SWORD_NAMES:
                return Sword()
            elif item_type_lower in self._ACCEPTABLE_SHIELD_NAMES:
                return Shield()
            elif item_type_lower in self._ACCEPTABLE_SHOES_NAMES:
                return Shoes()
            elif item_type_lower in self._ACCEPTABLE_HAT_NAMES:
                return SpookyHat()
            print "Did not recognize input: {}".format(item_type)