from unittest import TestCase
from main.managers.validate_sample_conflict_manager import ValidateSampleConflictManager
from main.managers.model_player_manager import ModelPlayerManager


class TestModelConflictManager(TestCase):

    def testStandardConflict(self):
        player_manager = ModelPlayerManager()
        player_manager.generate_players(0)
        conflict_manager = ValidateSampleConflictManager(player_manager)
        winner = conflict_manager.run()
        self.assertEqual(winner.NAME, "Alice")
        self.assertEqual(winner.HP, 4)
        self.assertEqual(len(winner.item_manager._SWORDS), 0)
        self.assertEqual(len(winner.item_manager._SHIELDS), 1)
        self.assertEqual(len(winner.item_manager._SHOES), 0)
        self.assertEqual(len(winner.item_manager._HATS), 1)

