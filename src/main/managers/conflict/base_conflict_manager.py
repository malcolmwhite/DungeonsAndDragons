import logging
from random import shuffle

from src.main.utils.utils import join_multi_line_strings


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

    def run_conflict(self):
        """
        Runs conflict. Conflict will continue until one player remains

        :return: (BasePlayer) winning player
        """
        active_players = self.player_manager.get_active_players()
        while len(active_players) > 1:
            self._run_round(active_players)
            active_players = self.player_manager.get_active_players()

        return active_players[0]

    def _determine_player_to_challenge(self, challenger, players):
        """
        Abstract method for specifying which player a given player will challenge
        :param challenger (BasePlayer): Player picking a player to challenge
        :param players: List of players to challenge
        :raise NotImplementedError: Method is abstract and must be overridden
        """
        raise NotImplementedError("_pick_conflict has not been implemented.")

    def _run_round(self, players):
        """
        Execute a round of conflicts for the given players.
        :param players: List of players
        """
        self.LOG.info("Beginning round.")
        players = self._order_players_for_new_round(players)
        challenge_map = self._build_challenge_map(players)
        for challenger in players:
            if self.player_manager.get_num_active_players() > 1:
                challenged = challenge_map[challenger]
                self._run_confrontation(challenger, challenged)

    def _build_challenge_map(self, players):
        """
        Maps players to the players they wish to challenge.
        Override :py:meth:`base_conflict_manager.BaseConflictManager._pick_conflict` to specify behavior
        :param players: list of challenging players
        :return: Map of challenging player to challenged player
        """
        challenge_map = dict()
        for index, challenger in enumerate(players):
            challenged = self._determine_player_to_challenge(challenger, players)
            challenge_map[challenger] = challenged
        return challenge_map

    def _run_confrontation(self, challenger, challenged):
        """
        Enact a confrontation between two players.
        :param challenger: Challenging player
        :param challenged: Challenged player
        """
        challenger.initialize_confrontation()
        challenged.initialize_confrontation()
        self.LOG.info("Beginning confrontation. %s challenging %s.", challenger.NAME, challenged.NAME)
        if not challenger.is_active():
            self.LOG.info("Challenger %s is not active.", challenger.NAME)
        elif not challenged.is_active():
            self.LOG.info("Challenged player %s is not active.", challenged.NAME)
        else:
            spook_rate, spook_power = challenged.get_spook_rate_and_power()
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
        BaseConflictManager._finalize_confrontation(challenger, challenged)

    @staticmethod
    def _finalize_confrontation(challenger, challenged):
        """
        Finalize players and log confrontation results.
        :param challenger: Challenging player
        :param challenged: Challenged player
        """
        challenger.finalize_confrontation()
        challenged.finalize_confrontation()
        BaseConflictManager._log_player_results(True, challenger, challenged)

    @staticmethod
    def _log_player_results(only_active, *players):
        """
        Log the summaries of the given players.
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

    def _order_players_for_new_round(self, players):
        # Sort players by priority
        players.sort(key=lambda p: p.get_round_priority(), reverse=True)
        # Shuffle within priorities
        left_index = 0
        last_priority = None
        for current_index, player in enumerate(players):
            current_priority = player.get_round_priority()
            if last_priority is not None:
                if last_priority is not current_priority:
                    right_index = current_index
                    self._shuffle_slice(players, left_index, right_index)
                    left_index = right_index
            last_priority = current_priority
        # shuffle the last section
        right_index = len(players) - 1
        self._shuffle_slice(players, left_index, right_index)
        log_msg = "Player order is: "
        for player in players:
            log_msg += player.NAME + ", "
        # Trim the final space and comma
        log_msg = log_msg[:-2]
        self.LOG.info(log_msg)

        return players

    @staticmethod
    def _validate_conflict_pair(challenger, challenged):
        return challenger.NAME.lower() != challenged.NAME.lower()

    @staticmethod
    def _shuffle_slice(container, left_index, right_index):
            slice_to_shuffle = container[left_index:right_index]
            shuffle(slice_to_shuffle)
            container[left_index:right_index] = slice_to_shuffle