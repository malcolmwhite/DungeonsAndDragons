import logging

from src.utils.utils import join_multi_line_strings


class BaseConflictManager(object):
    def __init__(self, player_manager):
        self.player_manager = player_manager
        self.LOG = logging.getLogger(__name__)
        logging.basicConfig(level=logging.DEBUG)

    def run(self):
        active_players = self.player_manager.get_active_players()
        while len(active_players) > 1:
            self._run_round(active_players)
            active_players = self.player_manager.get_active_players()

        return active_players[0]

    def _run_round(self, players):
        self.LOG.info("Beginning round.")
        players = self._sort_players(players)
        challenge_map = self._build_challenge_map(players)
        for challenger in players:
            if self.player_manager.get_num_active_players() > 1:
                challenged = challenge_map[challenger]
                self._run_conflict(challenger, challenged)

    def _build_challenge_map(self, players):
        challenge_map = dict()
        for index, challenger in enumerate(players):
            challenged = self._pick_conflict(challenger, players, index)
            challenge_map[challenger] = challenged
        return challenge_map

    def _run_conflict(self, challenger, challenged):
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
        challenger.finalize_conflict()
        challenged.finalize_conflict()
        BaseConflictManager._log_player_results(True, challenger, challenged)

    @staticmethod
    def _log_player_results(only_active, *players):
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
        raise NotImplementedError("_pick_conflict has not been implemented.")

    def _sort_players(self, players):
        raise NotImplementedError("_sort_players has not been implemented.")
