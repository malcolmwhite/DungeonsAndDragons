from src.main.managers.conflict.base_conflict_manager import BaseConflictManager


class ManualConflictManager(BaseConflictManager):
    def _determine_player_to_challenge(self, challenger, players):
        """
        Implementation of abstract method in BaseConflictManager.
        :param challenger: player determining who to challenge
        :param players: List of all players, including the challenger
        :return: player challenged by challenger
        """
        if len(players) == 2:
            return players[0] if players[0].NAME.lower() != challenger.NAME.lower() else players[1]

        print "Specify challenger for {}".format(challenger.NAME)
        print "Players are:"
        for player in players:
            if player is not challenger:
                print "\t" + player.NAME

        valid_input = False
        challenged = None
        while not valid_input:
            challenged_input = raw_input(
                "Please enter the name of the player to be challenged by {}.\n\t".format(challenger.NAME))
            input_name_lower = challenged_input.lower()
            selected_player = next((p for p in players if p.NAME == input_name_lower), None)
            if selected_player is None:
                print "Name [{}] not recognized.\n".format(challenged_input)
            elif self._validate_conflict_pair(challenger, selected_player):
                challenged = selected_player
                print "You have specified {} to be challenged by {}.".format(challenged.NAME, challenger.NAME)
                break
            else:
                print "Player {} cannot challenge player {}.".format(challenger.NAME, selected_player.NAME)
        return challenged

    def _run_round(self, players):
        raw_input("Press enter to begin round.")
        BaseConflictManager._run_round(self, players)