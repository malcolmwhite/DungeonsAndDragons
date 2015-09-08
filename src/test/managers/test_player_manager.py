from unittest import TestCase
from itertools import permutations

from src.main.managers.players.base_player_manager import BasePlayerManager
from src.main.beans.players.base_player import BasePlayer


class TestPlayerManager(TestCase):
    def test_add_players(self):
        player0 = BasePlayer(speed=100, name="FASTEST")
        player1 = BasePlayer(speed=5, name="Middle1")
        player2 = BasePlayer(speed=5, name="Middle2")
        player3 = BasePlayer(speed=1, name="SLOWEST")
        players = [player0, player1, player2, player3]

        for players_perm in permutations(players):
            players_perm = list(players_perm)
            player_manager = BasePlayerManager(players_perm)
            player_manager.sort_players(players_perm)
            self.validate_players(players_perm, player0, player1, player2, player3)

    def validate_players(self, players, player0, player1, player2, player3):
        self.assertEqual(players[0], player0)
        self.assertTrue((players[1] == player1) or (players[1] == player2))
        self.assertTrue((players[2] == player1) or (players[2] == player2))
        self.assertEqual(players[3], player3)
