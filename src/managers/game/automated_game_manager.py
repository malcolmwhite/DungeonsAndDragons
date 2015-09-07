from src.managers.game.base_game_manager import BaseGameManager
from src.managers.conflict.automated_conflict_manager import AutomatedConflictManager
from src.managers.players.base_player_manager import BasePlayerManager


class AutomatedGameManager(BaseGameManager):
    def _build_player_manager(self):
        return BasePlayerManager()

    def _build_conflict_manager(self, player_manager):
        return AutomatedConflictManager(player_manager)
