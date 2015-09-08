from random import randint

from src.main.managers.conflict.base_conflict_manager import BaseConflictManager


class AutomatedConflictManager(BaseConflictManager):
    def _pick_conflict(self, challenger, players, index):
        num_players = len(players)
        last_index = num_players - 1

        # reserve last index in case randint generates current index
        available_indices = last_index - 1
        challenged_index = randint(0, available_indices)
        if challenged_index == index:
            challenged_index = last_index

        return players[challenged_index]