from __future__ import division
from LineupGenerator import LineupGenerator
from LCSGeneralMultipliers import *

# ppg * matchup multiplier of performance range



TEAM_BLACKLIST = ()
PLAYER_BLACKLIST = ()


def LCSFormulaSix(lineup, player_holder):
    if not LineupGenerator.lineup_under_salary_cap(lineup):
        return 0
    else:
        fitness = get_lineup_player_scores(lineup, player_holder)
        team_multiplier = get_team_multiplier(lineup)
        games_multiplier = get_game_multiplier(lineup, player_holder.games)
        black_list_multipler = get_blacklist_muiltiplier(lineup, PLAYER_BLACKLIST, TEAM_BLACKLIST)
        return ((fitness * team_multiplier) * games_multiplier) * black_list_multipler

def get_player_score(player, player_holder):
    try:
        if player.standard_deviation == 0:
            return 0
        else:
            matchup_multiplier = get_matchup_multiplier(player, player_holder)
            player_best = max(player.week_performances)
            player_worst = min(player.week_performances)
            performance_range = player_best - player_worst
            return player.ppg *  ((player_worst + (performance_range * matchup_multiplier)) / player.average_performance)
    except:
        return player.ppg

def get_lineup_player_scores(lineup, player_holder):
    fitness = 0
    for p in lineup:
        fitness_score = get_player_score(p, player_holder)
        fitness += fitness_score
        p.special_stat = fitness_score
    return fitness

def get_matchup_multiplier(player, player_holder):
    game = None
    for g in player_holder.games:
        if player.team in g:
            game = g
    opposing_team = game[0 if game.index(player.team) == 1 else 1]
    opposing_team_object = [x for x in player_holder.team if x.team == opposing_team][0]
    player_team_object = [x for x in player_holder.team if x.team == player.team][0]
    total_wins = opposing_team_object.wins + player_team_object.wins
    return float(player_team_object.wins) / total_wins








