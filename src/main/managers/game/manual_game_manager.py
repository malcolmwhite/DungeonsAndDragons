from src.main.managers.game.base_game_manager import BaseGameManager
from src.main.managers.conflict.manual_conflict_manager import ManualConflictManager
from src.main.managers.players.manual_player_manager import ManualPlayerManager


class ManualGameManager(BaseGameManager):
    def _build_player_manager(self):
        return ManualPlayerManager()

    def _build_conflict_manager(self, player_manager):
        return ManualConflictManager(player_manager)
