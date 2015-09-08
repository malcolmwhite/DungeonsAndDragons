from src.utils.utils import raise_


class BaseGameManager(object):
    def __init__(self):
        player_manager = self._build_player_manager()
        conflict_manager = self._build_conflict_manager(player_manager)
        self.player_manager = player_manager
        self.conflict_manager = conflict_manager

    def run(self):
        return self.conflict_manager.run()

    def _build_player_manager(self):
        raise_(NotImplementedError("This function has not been implemented"))

    def _build_conflict_manager(self, player_manager):
        raise_(NotImplementedError("This function has not been implemented"))