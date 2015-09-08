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