from random import randint

from base_conflict_manager import BaseConflictManager
from automated_conflict_manager import AutomatedConflictManager


class ValidateSampleConflictManager(AutomatedConflictManager):
    ROUND_TO_REVERSE_MAP = {0: True, 1: False, 2:True}

    def __init__(self, player_manager):
        BaseConflictManager.__init__(self, player_manager)
        self.round = 0

    def _sort_players(self, players):
        if self.ROUND_TO_REVERSE_MAP[self.round]:
            player0 = players[0]
            players[0] = players[1]
            players[1] = player0
        self.round +=1
