import logging
from random import shuffle


class BasePlayerManager(object):
    def __init__(self, players=None):
        self.LOG = logging.getLogger(__name__)
        logging.basicConfig(level=logging.DEBUG)

        self._PLAYERS = []
        if players is not None:
            self.add_players(players)
        else:
            self.generate_players()

    def generate_players(self, num_players=None):
        raise NotImplementedError("Generate players has not been implemented.")

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
        if self._validate_new_player(player):
            self._PLAYERS.append(player)
            self.LOG.info("Added player:\n" + player.get_summary())

    def _validate_new_player(self, player):
        if not len(player.NAME):
            self.LOG.error("Players cannot have empty names.")
            return False
        for existing_player in self._PLAYERS:
            if existing_player.NAME.lower() == player.NAME.lower():
                self.LOG.error("Player with name " + player.NAME + " already exists.")
                return False
        return True

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
