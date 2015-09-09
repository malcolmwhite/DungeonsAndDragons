from src.main.managers.conflict.automated_conflict_manager import AutomatedConflictManager


class HardCodedExampleConflictManager(AutomatedConflictManager):
    ROUND_TO_REVERSE_MAP = {0: True, 1: False, 2: True}

    def __init__(self, player_manager):
        AutomatedConflictManager.__init__(self, player_manager)
        self.round = 0

    def _order_players_for_conflict(self, players):
        if self.ROUND_TO_REVERSE_MAP[self.round]:
            player0 = players[0]
            players[0] = players[1]
            players[1] = player0
        return players

    def _run_round(self, players):
        AutomatedConflictManager._run_round(self, players)
        self.round += 1
