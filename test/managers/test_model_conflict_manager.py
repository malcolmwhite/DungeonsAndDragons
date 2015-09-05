from unittest import TestCase
from main.managers.automated_conflict_manager import AutomatedConflictManager
from main.managers.model_player_manager import ModelPlayerManager

class TestModelConflictManager(TestCase):

    def testStandardConflict(self):
        player_manager = ModelPlayerManager()
        player_manager.generate_players(0)
        conflict_manager = AutomatedConflictManager(player_manager)
        conflict_manager.run()

