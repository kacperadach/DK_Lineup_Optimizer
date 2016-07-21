from random import randint
import copy
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SALARY_CAP = 50000


class LineupGenerator:

    def __init__(self, player_holder):
        self.player_holder = player_holder

    def get_random_valid_lineup(self):
        lineup = []
        lineup.append(self.player_holder.get_random_player("MID"))
        lineup.append(self.player_holder.get_random_player("TOP"))
        lineup.append(self.player_holder.get_random_player("JNG"))
        lineup.append(self.player_holder.get_random_player("ADC"))
        lineup.append(self.player_holder.get_random_player("SUP"))
        lineup.append(self.player_holder.get_random_player("TEAM"))
        player = self.player_holder.get_random_player("FLEX")
        for _ in range(0, 2):
            while player in lineup:
                player = self.player_holder.get_random_player("FLEX")
            lineup.append(player)
        return lineup

    @staticmethod
    def lineup_under_salary_cap(lineup):
        salary = 0
        for player in lineup:
            salary += int(player.salary)
        return salary <= SALARY_CAP

    def replace_player(self, lineup, second, pos):
        first_lineup = copy.copy(lineup)
        second_lineup = copy.copy(second)
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
            valid_positions = ("MID", "TOP", "JNG", "ADC", "SUP")
        else:
            valid_positions = (pos,)
        for p in lineup:
            if p.position in valid_positions and not LineupGenerator.player_in_lineup(p, new_lineup):
                lineup.remove(p)
                return p
        return None

    def merge_lineups(self, lineup, second, odds, random=False):
        first_lineup = copy.copy(lineup)
        second_lineup = copy.copy(second)
        if random is True:
            first_odds = odds
            second_odds = odds + ((100 - odds) / 2)
        else:
            first_odds = odds
            second_odds = 100

        positions = ("MID", "TOP", "JNG", "SUP", "ADC", "TEAM", "FLEX", "FLEX")
        new_lineup = []
        for x in range(0, 8):
            num = randint(0, 99)
            if num < first_odds:
                new_player = LineupGenerator.get_player_out_of_lineup(first_lineup, positions[x], new_lineup)
            elif num < second_odds:
                new_player = LineupGenerator.get_player_out_of_lineup(second_lineup, positions[x], new_lineup)
            else:
                new_player = self.player_holder.get_random_player(positions[x])
            while new_player is None or LineupGenerator.player_in_lineup(new_player, new_lineup):
                new_player = self.player_holder.get_random_player(positions[x])
            new_lineup.append(new_player)
        return new_lineup

    def print_players(self, position):
        for p in getattr(self.player_holder, position):
            if p.standard_deviation is not None:
                logger.info("{} {} {} {} {} {} {}".format(p.name, p.position, p.team, p.salary, p.ppg, p.standard_deviation, (p.ppg * (1 - p.standard_deviation))))
