from unittest import TestCase

from src.main.managers.players.base_player_manager import BasePlayerManager
from src.main.beans.players.base_player import BasePlayer


class TestPlayerManager(TestCase):
    def test_construct_with_players(self):
        player0 = BasePlayer(speed=100, name="FASTEST")
        player1 = BasePlayer(speed=5, name="Middle1")
        player2 = BasePlayer(speed=5, name="Middle2")
        player3 = BasePlayer(speed=1, name="SLOWEST")
        players = [player0, player1, player2, player3]

        player_manager = BasePlayerManager(players)
        self.validate_players(players, player_manager)

    def validate_players(self, players, player_manager):
        for player in players:
            self.assertTrue(player in player_manager._PLAYERS)
