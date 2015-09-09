from random import randint

from src.main.managers.conflict.base_conflict_manager import BaseConflictManager


class AutomatedConflictManager(BaseConflictManager):
    def _determine_player_to_challenge(self, challenger, players):
        """
        Implementation of abstract method in BaseConflictManager.
        :param challenger: player determining who to challenge. Argument not used for this implementation
        :param players: List of all players, including the challenger
        :return: player challenged by challenger
        """
        num_players = len(players)
        if num_players == 2:
            return players[0] if players[0].NAME.lower() != challenger.NAME.lower() else players[1]
        last_index = num_players - 1

        # Reserve last index in case randint generates current player's index
        available_indices = last_index - 1
        challenged_index = randint(0, available_indices)
        selected_player = players[challenged_index]
        if selected_player.NAME.lower() == challenger.NAME.lower():
            selected_player = players[last_index]

        return selected_player