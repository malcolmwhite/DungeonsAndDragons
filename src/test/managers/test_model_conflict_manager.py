from unittest import TestCase

from src.main.managers.players.hard_coded_player_manager import HardCodedPlayerManager
from src.main.managers.conflict.hard_coded_example_conflict_manager import HardCodedExampleConflictManager


class TestModelConflictManager(TestCase):
    def testStandardConflict(self):
        player_manager = HardCodedPlayerManager()
        conflict_manager = HardCodedExampleConflictManager(player_manager)
        winner = conflict_manager.run()
        self._validate_alice(winner)
        active_players = player_manager.get_active_players()
        inactive_players = player_manager.get_inactive_players()
        self.assertEqual(len(active_players), 1)
        self.assertEqual(len(inactive_players), 1)
        alice = active_players[0]
        bob = inactive_players[0]
        self._validate_alice(alice)
        self._validate_bob(bob)

    def _validate_alice(self, alice):
        self.assertEqual(alice.NAME, "Alice")
        self.assertEqual(alice.HP, 4)
        self.assertEqual(len(alice.item_manager._SWORDS), 0)
        self.assertEqual(len(alice.item_manager._SHIELDS), 1)
        self.assertEqual(len(alice.item_manager._SHOES), 0)
        self.assertEqual(len(alice.item_manager._HATS), 1)
        self.assertFalse(alice.is_spooked())

    def _validate_bob(self, bob):
        self.assertEqual(bob.NAME, "Bob")
        self.assertEqual(bob.HP, 0)
        self.assertEqual(len(bob.item_manager._SWORDS), 0)
        self.assertEqual(len(bob.item_manager._SHIELDS), 0)
        self.assertEqual(len(bob.item_manager._SHOES), 0)
        self.assertEqual(len(bob.item_manager._HATS), 0)
        self.assertFalse(bob.is_spooked())

        # class ValidateSampleConflictManager(AutomatedConflictManager):
        # ROUND_TO_REVERSE_MAP = {0: True, 1: False, 2:True}
        #
        #     def __init__(self, player_manager):
        #         AutomatedConflictManager.__init__(self, player_manager)
        #         self.round = 0
        #
        #     def _sort_players(self, players):
        #         if self.ROUND_TO_REVERSE_MAP[self.round]:
        #             player0 = players[0]
        #             players[0] = players[1]
        #             players[1] = player0
        #         return players
        #
        #     def _run_round(self, players):
        #         AutomatedConflictManager._run_round(self, players)
        #         self.round += 1

        # class HardCodedPlayerManager(BasePlayerManager):
        #     def generate_players(self, num_players):
        #         self.build_example_players()
        #
        #     def build_example_players(self):
        #         alice_hat = SpookyHat(spook_power=2, spook_rate=25)
        #         alice_item_manager = self.HardCodedAliceItemManager([alice_hat])
        #         alice = BasePlayer(item_manager=alice_item_manager, name="Alice", hp=5, defense=3, atk=7)
        #
        #         bob_shield = Shield(defense=1)
        #         bob_item_manager = ItemManager([bob_shield])
        #         bob = BasePlayer(item_manager=bob_item_manager, name="Bob", hp=8, defense=4, atk=5)
        #         self.add_player(alice)
        #         self.add_player(bob)
        #
        #     class HardCodedAliceItemManager(ItemManager):
        #         def __init__(self, items):
        #             ItemManager.__init__(self, items)
        #             self.first_run = True
        #
        #         def get_spook_params(self):
        #             power = 0
        #             if self._HATS:
        #                 hat = self._HATS[0]
        #                 hat_rate, hat_power = hat.get_spook_rate_and_power()
        #                 power += hat_power
        #             if self.first_run:
        #                 rate = 100
        #                 self.first_run = False
        #             else:
        #                 rate = 0
        #             return rate, power