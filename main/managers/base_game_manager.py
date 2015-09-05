from main.utils.utils import raise_


class BaseGameManager(object):

    def __init__(self):
        self.player_manager = None
        self.conflict_manager = None
        self._build_player_manager()
        self._build_conflict_manager(self.player_manager)

    def run(self):
        return self.conflict_manager.run()

    def _build_player_manager(self):
        raise_(NotImplementedError("This function has not been implemented"))

    def _build_conflict_manager(self, player_manager):
        raise_(NotImplementedError("This function has not been implemented"))