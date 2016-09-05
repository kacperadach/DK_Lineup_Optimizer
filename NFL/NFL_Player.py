

class NFLPlayer():

    def __init__(self, name, team, position, salary, ppg, projected_points=None):
        self.name = name
        self.team = team
        self.position = position
        self.salary = salary
        self.ppg = ppg
        self.projected_points = projected_points

    def update_projected_points(self, points):
        self.projected_points = points