def get_team_multiplier(lineup):
    teams = []
    for p in lineup:
        if p.position != "TEAM":
            teams.append(p.team)
    most_per_team = max([teams.count(x) for x in teams])
    if most_per_team <= 3:
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
    if len(games) == 2:
        limit = 5
    elif len(games) == 3:
        limit = 4
    else:
        limit = 3
    if most_per_game <= limit:
        return 1
    else:
        return 0

def get_blacklist_muiltiplier(lineup, player_blacklist, team_blacklist):
    black_list_boolean = False
    for p in lineup:
        if p in player_blacklist:
            black_list_boolean = True
        elif p.team in team_blacklist:
            black_list_boolean = True
    if black_list_boolean:
        return 0
    else:
        return 1
