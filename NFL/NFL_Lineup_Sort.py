def sort_lineup(lineup):
    sorted_lineup = []
    sorted_lineup.append(next(x for x in lineup if x.position == "QB"))
    sorted_lineup.append(next(x for x in lineup if x.position == "RB"))
    sorted_lineup.append(next(x for x in lineup if x.position == "RB" and x not in sorted_lineup))
    sorted_lineup.append(next(x for x in lineup if x.position == "WR"))
    sorted_lineup.append(next(x for x in lineup if x.position == "WR" and x not in sorted_lineup))
    sorted_lineup.append(next(x for x in lineup if x.position == "WR" and x not in sorted_lineup))
    sorted_lineup.append(next(x for x in lineup if x.position == "TE"))
    sorted_lineup.append(next(x for x in lineup if x.position != "DST" and x not in sorted_lineup))
    sorted_lineup.append(next(x for x in lineup if x.position == "DST"))
    return sorted_lineup
