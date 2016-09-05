from __future__ import division
from NFL.NFL_Lineup_Generator import NFLLineupGenerator
from NFLGeneralMultipliers import *
import numpy

# projected_points - st_dev of projected points

TEAM_BLACKLIST = ()
PLAYER_BLACKLIST = ()


def NFLFormulaThree(lineup, player_holder):
    if not NFLLineupGenerator.lineup_under_salary_cap(lineup):
        return 0
    else:
        fitness = get_lineup_player_scores(lineup)
        team_multiplier = get_team_multiplier(lineup)
        games_multiplier = get_game_multiplier(lineup, player_holder.games)
        black_list_multipler = get_blacklist_muiltiplier(lineup, PLAYER_BLACKLIST, TEAM_BLACKLIST)
        return fitness * team_multiplier * games_multiplier * black_list_multipler

def get_player_score(player):
    if player.projected_points:
        if player.ppg == 0:
            return 0
        return player.projected_points * (player.projected_points / player.ppg)
    else:
        return -100

def get_lineup_player_scores(lineup):
    fitness = []
    for p in lineup:
        fitness_score = get_player_score(p)
        fitness.append(fitness_score)
        p.special_stat = fitness_score
    return sum([(x - numpy.std(numpy.array(fitness))) for x in fitness])
