from src.main.utils.utils import query_yes_no
from src.main.managers.game.manual_game_manager import ManualGameManager

if __name__ == '__main__':
    while query_yes_no("Would you like to play a game?"):
        game_mgr = ManualGameManager()
        game_mgr.run()
