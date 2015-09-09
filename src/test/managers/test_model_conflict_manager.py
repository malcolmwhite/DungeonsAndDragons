from unittest import TestCase
from itertools import permutations

from src.main.managers.players.hard_coded_player_manager import HardCodedPlayerManager
from src.main.managers.conflict.hard_coded_example_conflict_manager import HardCodedExampleConflictManager
from src.main.managers.conflict.automated_conflict_manager import AutomatedConflictManager
from src.main.beans.players.standard_player import StandardPlayer
from src.main.managers.players.base_player_manager import BasePlayerManager


class TestModelConflictManager(TestCase):
    def testStandardConflict(self):
        player_manager = HardCodedPlayerManager()
        conflict_manager = HardCodedExampleConflictManager(player_manager)
        winner = conflict_manager.run_conflict()
        self._validate_alice(winner)
        active_players = player_manager.get_active_players()
        inactive_players = player_manager.get_inactive_players()
        self.assertEqual(len(active_players), 1)
        self.assertEqual(len(inactive_players), 1)
        alice = active_players[0]
        bob = inactive_players[0]
        self._validate_alice(alice)
        self._validate_bob(bob)

    def test_add_players(self):
        player0 = StandardPlayer(speed=100, name="FASTEST")
        player1 = StandardPlayer(speed=5, name="Middle1")
        player2 = StandardPlayer(speed=5, name="Middle2")
        player3 = StandardPlayer(speed=1, name="SLOWEST")
        players = [player0, player1, player2, player3]

        for players_perm in permutations(players):
            players_perm = list(players_perm)
            player_manager = BasePlayerManager(players_perm)
            conflict_manager = AutomatedConflictManager(player_manager)
            sorted_players = conflict_manager._order_players_for_new_round(players_perm)
            self.validate_players(sorted_players, player0, player1, player2, player3)

    def validate_players(self, players, player0, player1, player2, player3):
        self.assertEqual(players[0], player0)
        self.assertTrue((players[1] == player1) or (players[1] == player2))
        self.assertTrue((players[2] == player1) or (players[2] == player2))
        self.assertEqual(players[3], player3)

    def _validate_alice(self, alice):
        self.assertEqual(alice.NAME, "Alice")
        self.assertEqual(alice.HP, 4)
        self.assertEqual(len(alice.item_manager._SWORD_BAG), 0)
        self.assertEqual(len(alice.item_manager._SHIELD_BAG), 1)
        self.assertEqual(len(alice.item_manager._SHOES_BAG), 0)
        self.assertEqual(len(alice.item_manager._HAT_BAG), 1)
        self.assertFalse(alice.is_spooked())

    def _validate_bob(self, bob):
        self.assertEqual(bob.NAME, "Bob")
        self.assertEqual(bob.HP, 0)
        self.assertEqual(len(bob.item_manager._SWORD_BAG), 0)
        self.assertEqual(len(bob.item_manager._SHIELD_BAG), 0)
        self.assertEqual(len(bob.item_manager._SHOES_BAG), 0)
        self.assertEqual(len(bob.item_manager._HAT_BAG), 0)
        self.assertFalse(bob.is_spooked())