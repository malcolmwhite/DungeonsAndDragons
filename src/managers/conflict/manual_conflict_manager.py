from src.managers.conflict.base_conflict_manager import BaseConflictManager
from ..players.base_player_manager import BasePlayerManager

class ManualConflictManager(BaseConflictManager):
    def _pick_conflict(self, challenger, players, index):
        print "Specify challenger for {}".format(challenger.NAME)
        print "Players are:"
        for player in players:
            if player is not challenger:
                print player.NAME

        valid_input = False
        challenged = None
        while not valid_input:
            challenged_input = raw_input("Please enter the name of the player to be challenged by {}.".format(challenger.NAME))
            for player in players:
                if player.NAME.lower() == challenged_input:
                    if player == challenger:
                        print "A player cannot challenge his or her self. Please pick a different player."
                        break
                    challenged = player
                    print "You have specified {} to be challenged by {}.".format(challenged.NAME, challenger.NAME)
                    valid_input = True
                    break

        return challenged

    def _sort_players(self, players):
        ordered_players = BasePlayerManager.sort_players(players)
        print "player order is ", ordered_players
        return ordered_players
        # print "Specify order for players in this round."
        # print "Players are:"
        # for index, player in enumerate(players):
        #     print index, player.NAME
        # valid_input = False
        # order = []
        # while not valid_input:
        #     order_input = raw_input("Please enter player indices in the order they will act.")
        #     order = order_input.split()
        #     order = [int(i) for i in order]
        #     valid_input = self._validate_order_input(players, order)
        #
        # ordered_players = [players[i] for i in order]
        # return ordered_players


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