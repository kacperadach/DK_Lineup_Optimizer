from __future__ import division
from LineupGenerator import LineupGenerator


def LCSFormulaOne(lineup):
    if not LineupGenerator.lineup_under_salary_cap(lineup):
        return 0
    else:
        fitness = get_lineup_player_scores(lineup)
        team_multiplier = get_multipliers(lineup)
        return fitness * team_multiplier

def get_player_score(player):
    try:
        if player.position == "TEAM":
            return player.ppg
        elif player.standard_deviation == 0:
            return 0
        else:
            return (player.ppg * (1 - player.standard_deviation))
    except:
        return player.ppg

def get_lineup_player_scores(lineup):
    fitness = 0
    for p in lineup:
        fitness += get_player_score(p)
    return fitness

def get_multipliers(lineup):
    teams = []
    for p in lineup:
        if p.position != "TEAM":
            teams.append(p.team)
    most_per_team = max([teams.count(x) for x in teams])
    return get_players_per_team_multiplier(most_per_team)

def get_players_per_team_multiplier(most_per_team):
    if most_per_team <= 3:
        return 1
    else:
        return (-1 * (most_per_team / 6)) + (4 / 3)

