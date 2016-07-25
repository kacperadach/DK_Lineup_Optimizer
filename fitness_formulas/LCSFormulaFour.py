from __future__ import division
from LineupGenerator import LineupGenerator


TEAM_BLACKLIST = ()
PLAYER_BLACKLIST = ()


def LCSFormulaFour(lineup, games):
    if not LineupGenerator.lineup_under_salary_cap(lineup):
        return 0
    else:
        fitness = get_lineup_player_scores(lineup)
        team_multiplier = get_team_multiplier(lineup)
        games_multiplier = get_game_multiplier(lineup, games)
        black_list_multipler = get_blacklist_muiltiplier(lineup)
        return (fitness * team_multiplier) * black_list_multipler

def get_player_score(player):
    try:
        return player.ppg
    except:
        return player.ppg

def get_lineup_player_scores(lineup):
    fitness = 0
    for p in lineup:
        fitness_score = get_player_score(p)
        fitness += fitness_score
        p.special_stat = fitness_score
    return fitness

def get_team_multiplier(lineup):
    teams = []
    for p in lineup:
        if p.position != "TEAM":
            teams.append(p.team)
    most_per_team = max([teams.count(x) for x in teams])
    if most_per_team <= 4:
        return 1
    else:
        return 0

def get_game_multiplier(lineup, games):
    game_array = []
    for p in lineup:
        for game in games:
            if p.team in game:
                game_array.append(games.index(game))
    most_per_game = max([game_array.count(x) for x in game_array])
    if most_per_game <= 3:
        return 1
    else:
        return 0

def get_blacklist_muiltiplier(lineup):
    black_list_boolean = False
    for p in lineup:
        if p in PLAYER_BLACKLIST:
            black_list_boolean = True
        elif p.team in TEAM_BLACKLIST:
            black_list_boolean = True
    if black_list_boolean:
        return 0
    else:
        return 1
