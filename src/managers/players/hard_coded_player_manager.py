from src.managers.items.item_manager import ItemManager
from src.managers.items.hard_coded_alice_item_manager import HardCodedAliceItemManager
from src.managers.players.base_player_manager import BasePlayerManager
from src.beans.players.base_player import BasePlayer
from src.beans.items.spooky_hat import SpookyHat
from src.beans.items.shield import Shield


class HardCodedPlayerManager(BasePlayerManager):

        def generate_players(self, num_players=None):
            alice_hat = SpookyHat(spook_power=2, spook_rate=25)
            alice_item_manager = HardCodedAliceItemManager([alice_hat])
            alice = BasePlayer(item_manager=alice_item_manager, name="Alice", hp=5, defense=3, atk=7)
            self.add_player(alice)

            bob_shield = Shield(defense=1)
            bob_item_manager = ItemManager([bob_shield])
            bob = BasePlayer(item_manager=bob_item_manager, name="Bob", hp=8, defense=4, atk=5)
            self.add_player(bob)

