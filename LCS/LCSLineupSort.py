def sort_lineup(lineup):
    sorted_lineup = []
    sorted_lineup.append(next(x for x in lineup if x.position == "TOP"))
    sorted_lineup.append(next(x for x in lineup if x.position == "JNG"))
    sorted_lineup.append(next(x for x in lineup if x.position == "MID"))
    sorted_lineup.append(next(x for x in lineup if x.position == "ADC"))
    sorted_lineup.append(next(x for x in lineup if x.position == "SUP"))
    sorted_lineup.append(next(x for x in lineup if x.position != "TEAM" and x not in sorted_lineup))
    sorted_lineup.append(next(x for x in lineup if x.position != "TEAM" and x not in sorted_lineup))
    sorted_lineup.append(next(x for x in lineup if x.position == "TEAM"))
    return sorted_lineup
