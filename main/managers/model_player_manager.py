from base_player_manager import BasePlayerManager
from item_manager import ItemManager
from main.players.base_player import BasePlayer
from main.items.spooky_hat import SpookyHat
from main.items.shield import Shield


class ModelPlayerManager(BasePlayerManager):
    def generate_players(self, num_players):
        self.build_example_players()

    def build_example_players(self):
        alice_hat = SpookyHat(spook_power=2, spook_rate=100)
        alice_item_manager = ItemManager([alice_hat])
        alice = BasePlayer(item_manager=alice_item_manager, name="Alice", hp=5, defense=3, atk=7)

        bob_shield = Shield(defense=1)
        bob_item_manager = ItemManager([bob_shield])
        bob = BasePlayer(item_manager=bob_item_manager, name="Bob", hp=10, defense=4, atk=5)
        self._add_player(alice)
        self._add_player(bob)