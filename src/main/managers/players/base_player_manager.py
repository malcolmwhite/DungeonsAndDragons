import logging


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
