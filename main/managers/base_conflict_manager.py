from main.utils.utils import get_trimmed_or_padded_string
import logging
from itertools import izip_longest


class BaseConflictManager(object):

    def __init__(self, player_manager):
        self.player_manager = player_manager
        logging.basicConfig(level=logging.DEBUG)

    def run(self):
        active_players = self.player_manager.get_active_players()
        while len(active_players) > 1:
            self._run_round(active_players)
            active_players = self.player_manager.get_active_players()

        return active_players[0]

    def _run_round(self, players):
        logging.info("Beginning round.")
        self._sort_players(players)
        challenge_map = self._build_challenge_map(players)
        for challenger, challenged in challenge_map.iteritems():
            self._run_conflict(challenger, challenged)

    def _build_challenge_map(self, players):
        challenge_map = dict()
        for index, challenger in enumerate(players):
            challenged = self._pick_conflict(challenger, players, index)
            challenge_map[challenger] = challenged
        return challenge_map

    @staticmethod
    def _run_conflict(challenger, challenged):
        challenger.initialize_conflict()
        challenged.initialize_conflict()
        logging.info("Beginning conflict. %s challenging %s.", challenger.NAME, challenged.NAME)
        if not challenger.is_active():
            logging.info("Challenger %s is not active.", challenger.NAME)
        elif not challenged.is_active():
            logging.info("Challenged player %s is not active.", challenged.NAME)
        else:
            spook_rate, spook_power = challenged.get_spook_params()
            spook_success = challenger.receive_spook(spook_rate, spook_power)
            if spook_success:
                logging.info("%s spooked %s.", challenged.NAME, challenger.NAME)
            attack_points = challenger.get_effective_attack()
            damage_inflicted = challenged.receive_attack(attack_points)
            logging.info("%s inflicted %d damage to %s.", challenger.NAME, damage_inflicted, challenged.NAME)
            if not challenged.is_active():
                logging.info("%s is no longer active. Items pass to %s.", challenged.NAME, challenger.NAME)
                items_won = challenged.dump_all_items()
                challenger.add_items(items_won)
        BaseConflictManager._finalize_conflict(challenger, challenged)

    @staticmethod
    def _finalize_conflict(challenger, challenged):
        challenger.finalize_conflict()
        challenged.finalize_conflict()
        BaseConflictManager._log_conflict_results(True, challenger, challenged)

    @staticmethod
    def _log_conflict_results(only_active, *players):
        cell_width = 25
        overall_result = []
        attributes = ["get_formatted_name", "get_formatted_attack", "get_formatted_defense", "get_formatted_hp", "get_formatted_items"]
        for player in players:
            if player.is_active():
                player_result = ""
                for attribute in attributes:
                    attribute_line = BaseConflictManager._get_conflict_value(player, attribute, cell_width)
                    player_result += attribute_line + "\n"
                overall_result.append(player_result)
        print BaseConflictManager._join_multi_line_strings(overall_result, cell_width)

    @staticmethod
    def _get_conflict_value(player, attribute, cell_width):
        value = getattr(player, attribute)()
        value = value.splitlines()
        result = ""
        for line in value:
            result += get_trimmed_or_padded_string(line, cell_width) + "\n"
        return result[:-1]

    @staticmethod
    def _join_multi_line_strings(blocks, cell_width):
        output = ""
        while blocks:
            left = blocks.pop()
            right = blocks.pop() if blocks else ""
            left = left.splitlines()
            right = right.splitlines()
            if_missing = " "*cell_width
            for left_line, right_line in izip_longest(left, right, fillvalue=if_missing):
                output += left_line + right_line + "\n"
        return output[:-1]

    def _pick_conflict(self, challenger, players, index):
        raise NotImplementedError("_pick_conflict has not been implemented.")

    def _sort_players(self, players):
        raise NotImplementedError("_sort_players has not been implemented.")
