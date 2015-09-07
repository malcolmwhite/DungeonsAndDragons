import logging

from src.utils.utils import join_multi_line_strings


class BaseConflictManager(object):
    """
    Abstract class with core functionality for managing conflicts.
    Implementations must implement :py:meth:`base_conflict_manager.BaseConflictManager._pick_conflict` and
    :py:meth:`base_conflict_manager.BaseConflictManager._sort_players`.

    Attributes:
        player_manager (Implementation of BasePlayerManager): Builds and maintains collection of players
    """

    def __init__(self, player_manager):
        self.player_manager = player_manager
        self.LOG = logging.getLogger(__name__)
        logging.basicConfig(level=logging.DEBUG)

    def run(self):
        """
        Begin conflicts. Conflicts will continue until one player remains

        :return: (BasePlayer) winning player
        """
        active_players = self.player_manager.get_active_players()
        while len(active_players) > 1:
            self._run_round(active_players)
            active_players = self.player_manager.get_active_players()

        return active_players[0]

    def _run_round(self, players):
        """
        Execute a round of conflicts for the given players.
        :param players: List of players
        """
        self.LOG.info("Beginning round.")
        players = self._sort_players(players)
        challenge_map = self._build_challenge_map(players)
        for challenger in players:
            if self.player_manager.get_num_active_players() > 1:
                challenged = challenge_map[challenger]
                self._run_conflict(challenger, challenged)

    def _build_challenge_map(self, players):
        """
        Maps players to the players they wish to challenge.
        Override :py:meth:`base_conflict_manager.BaseConflictManager._pick_conflict` to specify behavior
        :param players: list of challenging players
        :return: Map of challenging player to challenged player
        """
        challenge_map = dict()
        for index, challenger in enumerate(players):
            challenged = self._pick_conflict(challenger, players, index)
            challenge_map[challenger] = challenged
        return challenge_map

    def _run_conflict(self, challenger, challenged):
        """
        Enact a conflict between two players.
        :param challenger: Challenging player
        :param challenged: Challenged player
        """
        challenger.initialize_conflict()
        challenged.initialize_conflict()
        self.LOG.info("Beginning conflict. %s challenging %s.", challenger.NAME, challenged.NAME)
        if not challenger.is_active():
            self.LOG.info("Challenger %s is not active.", challenger.NAME)
        elif not challenged.is_active():
            self.LOG.info("Challenged player %s is not active.", challenged.NAME)
        else:
            spook_rate, spook_power = challenged.get_spook_params()
            spook_success = challenger.receive_spook(spook_rate, spook_power)
            if spook_success:
                self.LOG.info("%s spooked %s.", challenged.NAME, challenger.NAME)
            attack_points = challenger.get_effective_attack()
            damage_inflicted = challenged.receive_attack(attack_points)
            self.LOG.info("%s inflicted %d damage to %s.", challenger.NAME, damage_inflicted, challenged.NAME)
            if not challenged.is_active():
                self.LOG.info("%s has defeated %s and takes all of their items.", challenger.NAME, challenged.NAME)
                items_won = challenged.dump_all_items()
                challenger.add_items(items_won)
        BaseConflictManager._finalize_conflict(challenger, challenged)

    @staticmethod
    def _finalize_conflict(challenger, challenged):
        """
        Finalize players and log conflict results.
        :param challenger: Challenging player
        :param challenged: Challenged player
        """
        challenger.finalize_conflict()
        challenged.finalize_conflict()
        BaseConflictManager._log_player_results(True, challenger, challenged)

    @staticmethod
    def _log_player_results(only_active, *players):
        """
        Log the results of a conflict.
        :param only_active (bool): Indicates if results should only be shown for active players
        :param players: List of players
        """
        players = list(players)
        players.sort(key=lambda p: p.NAME)
        cell_width = 25
        overall_summary = []

        for player in players:
            if player.is_active() or not only_active:
                player_summary = player.get_summary()
                overall_summary.append(player_summary)
        print join_multi_line_strings(overall_summary, cell_width)

    def _pick_conflict(self, challenger, players, index):
        """
        Abstract method for specifying which player a given player will challenge
        :param challenger (BasePlayer): Player picking a player to challenge
        :param players: List of players to challenge
        :param index: challenger's index. Value used to ensure the challenger does not challenge his/herself
        :raise NotImplementedError: Method is abstract and must be overridden
        """
        raise NotImplementedError("_pick_conflict has not been implemented.")

    def _sort_players(self, players):
        """
        Abstract method for sorting players before a round.
        :param players: List of players
        :raise NotImplementedError: Method is abstract and must be overridden
        """
        raise NotImplementedError("_sort_players has not been implemented.")
