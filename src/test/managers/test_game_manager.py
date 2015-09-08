from unittest import TestCase

from src.managers.conflict.hard_coded_example_conflict_manager import HardCodedExampleConflictManager
from src.main.managers.game.base_game_manager import BaseGameManager
from src.managers.players.hard_coded_player_manager import HardCodedPlayerManager


class TestGameManager(TestCase):
    def testStandardGame(self):
        game_manager = self.ExampleGameManager()
        winner = game_manager.run()
        self._validate_alice(winner)
        active_players = game_manager.player_manager.get_active_players()
        inactive_players = game_manager.player_manager.get_inactive_players()
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

    class ExampleGameManager(BaseGameManager):
        def _build_player_manager(self):
            return HardCodedPlayerManager()

        def _build_conflict_manager(self, player_manager):
            return HardCodedExampleConflictManager(player_manager)