from src.main.managers.conflict.base_conflict_manager import BaseConflictManager


class ManualConflictManager(BaseConflictManager):
    def _determine_player_to_challenge(self, challenger, players, index):
        if len(players) == 2:
            return players[0] if players[0] != challenger else players[1]

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
            for player in players:
                if player.NAME.lower() == challenged_input.lower():
                    if player == challenger:
                        print "A player cannot challenge his or her self. Please pick a different player."
                        break
                    challenged = player
                    print "You have specified {} to be challenged by {}.".format(challenged.NAME, challenger.NAME)
                    valid_input = True
                    break
            if not valid_input:
                print "Name [{}] not recognized.\n".format(challenged_input)

        return challenged

    def _run_round(self, players):
        BaseConflictManager._run_round(self, players)
        print "The results of the round are:"
        self._log_player_results(False, *players)

    @staticmethod
    def _validate_order_input(players, order):
        num_players = len(players)
        order_set = set(order)
        num_specified_indices = len(order)
        num_unique_indices = len(order_set)
        min_index = min(order_set)
        max_index = max(order_set)
        min_allowable_index = 0
        max_allowable_index = num_players - 1
        if num_specified_indices > num_players:
            print "You must specify", num_players, "indices. You specified", num_specified_indices
            print "Specified list was: " + order
            return False
        elif num_unique_indices != num_players:
            print "You must specify", num_players, " unique indices. You specified", num_specified_indices
            print "Specified list was: " + order
            return False
        elif max_index > max_allowable_index:
            print "You must not specify an index greater than ", max_allowable_index, " You specified", max_index
            print "Specified list was: " + order
            return False
        elif min_index > min_allowable_index:
            print "You must not specify an index less than ", min_allowable_index, " You specified", min_index
            print "Specified list was: " + order
            return False
        return True