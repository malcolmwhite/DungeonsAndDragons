from random import shuffle


class BasePlayerManager(object):
    def __init__(self, players=None):
        self._PLAYERS = []
        if players is not None:
            self.add_players(players)
        else:
            self.generate_players()

    def generate_players(self, num_players=None):
        raise NotImplementedError("Generate players has not been implemented.")

    def initialize_round(self, shuffle_players=True):
        # Sort players by priority
        BasePlayerManager.sort_players(self._PLAYERS)
        # Shuffle priorities

    def get_active_players(self):
        return [player for player in self._PLAYERS if player.is_active()]

    def get_inactive_players(self):
        return [player for player in self._PLAYERS if not player.is_active()]

    def get_num_active_players(self):
        return len(self.get_active_players())

    def add_players(self, players):
        for player in players:
            self.add_player(player)

    def add_player(self, player):
        self._PLAYERS.append(player)

    @staticmethod
    def sort_players(players):
        # Sort players by priority
        players.sort(key=lambda p: p.get_conflict_priority(), reverse=True)
        # Shuffle within priorities
        left_index = 0
        last_priority = None
        for current_index, player in enumerate(players):
            current_priority = player.get_conflict_priority()
            if last_priority is not None:
                if last_priority is not current_priority:
                    right_index = current_index - 1
                    shuffle(players[left_index:right_index])
                    left_index = current_index
            last_priority = current_priority
        # shuffle the last section
        right_index = len(players) - 1
        shuffle(players[left_index:right_index])
        return players
