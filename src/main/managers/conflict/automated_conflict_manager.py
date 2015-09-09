from random import randint

from src.main.managers.conflict.base_conflict_manager import BaseConflictManager


class AutomatedConflictManager(BaseConflictManager):
    def _determine_player_to_challenge(self, challenger, players, challenger_index):
        """
        Implementation of abstract method in BaseConflictManager.
        :param challenger: player determining who to challenge. Argument not used for this implementation
        :param players: List of all players, including the challenger
        :param challenger_index: index of challenger in players
        :return: player challenged by challenger
        """
        num_players = len(players)
        if num_players == 2:
            return players[not challenger_index]
        last_index = num_players - 1

        # reserve last index in case randint generates current index
        available_indices = last_index - 1
        challenged_index = randint(0, available_indices)
        if challenged_index == challenger_index:
            challenged_index = last_index

        return players[challenged_index]