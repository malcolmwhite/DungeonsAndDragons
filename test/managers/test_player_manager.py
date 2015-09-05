from unittest import TestCase
from main.managers.base_player_manager import BasePlayerManager
from main.players.base_player import BasePlayer


class TestPlayerManager(TestCase):

    def test_add_players(self):
        player_manager = BasePlayerManager()
        player0 = BasePlayer(speed=100, name="FASTEST")
        player1 = BasePlayer(speed=5, name="Middle1")
        player2 = BasePlayer(speed=5, name="Middle2")
        player3 = BasePlayer(speed=1, name="SLOWEST")
        players = [player0, player1, player2, player3]
        player_manager.add_players(players)
        player_manager.sort_players(players)
        self.validate_players(players, player0, player1, player2, player3)

        player_manager = BasePlayerManager()
        players = [player3, player1, player2, player0]
        player_manager.add_players(players)
        player_manager.sort_players(players)
        self.validate_players(players, player0, player1, player2, player3)

        player_manager = BasePlayerManager()
        players = [player3, player2, player1, player0]
        player_manager.add_players(players)
        player_manager.sort_players(players)
        self.validate_players(players, player0, player1, player2, player3)

    def validate_players(self, players, player0, player1, player2, player3):
        self.assertEqual(players[0], player0)
        self.assertTrue((players[1] == player1) or (players[1] == player2))
        self.assertTrue((players[2] == player1) or (players[2] == player2))
        self.assertEqual(players[3], player3)
