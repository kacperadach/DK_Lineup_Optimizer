from random import randint
from copy import copy
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from constants import SALARY_CAP, GET_ITERABLE_VALID_LINEUP, FLEX_POSITIONS, POSITIONS


class NFLLineupGenerator:

    def __init__(self, player_holder):
        self.player_holder = player_holder

    def get_random_valid_lineup(self):
        lineup = []
        for position in GET_ITERABLE_VALID_LINEUP():
            player = self.player_holder.get_random_player(position)
            if player not in lineup:
                lineup.append(player)
        return lineup

    @staticmethod
    def lineup_under_salary_cap(lineup):
        salary = 0
        for player in lineup:
            salary += int(player.salary)
        return salary <= SALARY_CAP

    def replace_player(self, lineup, second, pos):
        first_lineup = copy(lineup)
        second_lineup = copy(second)
        for p in first_lineup:
            if p.position.upper() == pos.upper():
                first_lineup.remove(p)
                break
        replacement = None
        for p in second_lineup:
            if p.position.upper() == pos.upper():
                if p not in first_lineup:
                    replacement = p
                    break
        if replacement is None:
            replacement = self.player_holder.get_random_player(pos)
        first_lineup.append(replacement)
        return first_lineup

    @staticmethod
    def player_in_lineup(player, lineup):
        name = player.name
        for p in lineup:
            if p.name.upper() == name.upper():
                return True
        return False

    @staticmethod
    def get_player_out_of_lineup(lineup, pos, new_lineup):
        if pos.upper() == "FLEX":
            valid_positions = FLEX_POSITIONS
        else:
            valid_positions = (pos,)
        for p in lineup:
            if p.position in valid_positions and not NFLLineupGenerator.player_in_lineup(p, new_lineup):
                lineup.remove(p)
                return p
        return None

    def merge_lineups(self, lineup, second, odds, random=False):
        first_lineup = copy(lineup)
        second_lineup = copy(second)
        if random is True:
            first_odds = odds
            second_odds = odds + ((100 - odds) / 2)
        else:
            first_odds = odds
            second_odds = 100

        positions = GET_ITERABLE_VALID_LINEUP()
        new_lineup = []
        for x in range(0, len(positions)):
            num = randint(0, 99)
            if num < first_odds:
                new_player = NFLLineupGenerator.get_player_out_of_lineup(first_lineup, positions[x], new_lineup)
            elif num < second_odds:
                new_player = NFLLineupGenerator.get_player_out_of_lineup(second_lineup, positions[x], new_lineup)
            else:
                new_player = self.player_holder.get_random_player(positions[x])
            while new_player is None or NFLLineupGenerator.player_in_lineup(new_player, new_lineup):
                new_player = self.player_holder.get_random_player(positions[x])
            new_lineup.append(new_player)
        return new_lineup

    def print_players(self, position):
        if position.upper() == "ALL":
            pos = POSITIONS
        else:
            pos = (position,)
        for s in pos:
            logger.info("")
            for p in getattr(self.player_holder, s):
                logger.info("{} {} {} {} {} {}".format(p.name, p.position, p.team, p.salary, p.ppg, p.projected_points))
