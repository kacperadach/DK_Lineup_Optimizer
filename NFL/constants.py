TEAM_MATCHER = {
    'Green Bay': 'Packers',
    'Los Angeles': 'Rams',
    'Kansas City': 'Chiefs',
    'New York': 'Jets',
    'New England': 'Patriots',
    'New York': 'Giants',
    'Tampa Bay': 'Buccaneers',
    'San Francisco': '49ers',
    'New Orleans': 'Saints',
    'San Diego': 'Chargers'
}

SALARY_CAP = 50000

POSITIONS = ['QB', 'RB', 'WR', 'TE', 'DST']

POSITIONS_WITH_FLEX = ['QB', 'RB', 'WR', 'TE', 'DST', 'FLEX']

FLEX_POSITIONS = ['RB', 'WR', 'TE']

VALID_LINEUP_POSITIONS = {
    'QB': 1,
    'RB': 2,
    'WR': 3,
    'TE': 1,
    'FLEX': 1,
    'DST': 1
}

def GET_ITERABLE_VALID_LINEUP():
    return [key for key, val in VALID_LINEUP_POSITIONS.items() for _ in range(0, val)]