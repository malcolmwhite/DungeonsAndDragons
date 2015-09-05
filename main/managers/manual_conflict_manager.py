from random import randint

from base_conflict_manager import BaseConflictManager


class ManualConflictManager(BaseConflictManager):
    def _pick_conflict(self, challenger, players, index):
        num_players = len(players)
        last_index = num_players - 1

        # reserve last index in case randint generates current index
        available_indices = last_index - 1
        challenged_index = randint(0, available_indices)
        if challenged_index == index:
            challenged_index = last_index

        return players[challenged_index]

    def _sort_players(self, players):
        print "Specify order for players in this round."
        print "Players are:"
        for index, player in enumerate(players):
            print index, player.NAME
        valid_input = False
        order = []
        while not valid_input:
            order_input = raw_input("Please enter player indices in the order they will act.")
            order = order_input.split()
            order = [int(i) for i in order]
            valid_input = self._validate_input(players, order)

        ordered_players = [players[i] for i in order]


    @staticmethod
    def _validate_input(players, order):
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