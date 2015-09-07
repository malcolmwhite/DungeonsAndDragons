from main.managers.items.item_manager import ItemManager
from main.managers.items.hard_coded_alice_item_manager import HardCodedAliceItemManager
from main.managers.players.base_player_manager import BasePlayerManager
from main.beans.players.base_player import BasePlayer
from main.beans.items.spooky_hat import SpookyHat
from main.beans.items.shield import Shield


class HardCodedPlayerManager(BasePlayerManager):
        def __init__(self):
            BasePlayerManager.__init__(self, None)
            self.build_example_players()

        def generate_players(self, num_players=None):
            self.build_example_players()

        def build_example_players(self):
            alice_hat = SpookyHat(spook_power=2, spook_rate=25)
            alice_item_manager = HardCodedAliceItemManager([alice_hat])
            alice = BasePlayer(item_manager=alice_item_manager, name="Alice", hp=5, defense=3, atk=7)

            bob_shield = Shield(defense=1)
            bob_item_manager = ItemManager([bob_shield])
            bob = BasePlayer(item_manager=bob_item_manager, name="Bob", hp=8, defense=4, atk=5)
            self.add_player(alice)
            self.add_player(bob)

