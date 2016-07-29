from __future__ import division
from LineupGenerator import LineupGenerator
from LCSGeneralMultipliers import *

# ppg - stdev


TEAM_BLACKLIST = ()
PLAYER_BLACKLIST = ()


def LCSFormulaOne(lineup, games):
    if not LineupGenerator.lineup_under_salary_cap(lineup):
        return 0
    else:
        fitness = get_lineup_player_scores(lineup)
        team_multiplier = get_team_multiplier(lineup)
        games_multiplier = get_game_multiplier(lineup, games)
        black_list_multipler = get_blacklist_muiltiplier(lineup, PLAYER_BLACKLIST, TEAM_BLACKLIST)
        return ((fitness * team_multiplier) * games_multiplier) * black_list_multipler

def get_player_score(player):
    try:
        if player.standard_deviation == 0:
            return 0
        else:
            return (player.ppg * (1 - player.standard_deviation))
    except:
        return player.ppg

def get_lineup_player_scores(lineup):
    fitness = 0
    for p in lineup:
        fitness_score = get_player_score(p)
        fitness += fitness_score
        p.special_stat = fitness_score
    return fitness
