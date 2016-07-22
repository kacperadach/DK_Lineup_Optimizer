import math

class Player:

    def __init__(self, name, team, position, salary, ppg):
        self.name = name.strip()
        self.team = team
        self.position = position
        self.salary = int(salary)
        self.ppg = float(ppg)
        self.week_performances = []
        self.average_performance = None
        self.standard_deviation = None

    def calculate_stan_dev(self):
        mean = self.average_performance
        if mean is None:
            return
        total = 0
        for wp in self.week_performances:
            total += ((wp - mean) * (wp - mean))
        if len(self.week_performances) == 0 or mean == 0:
            self.standard_deviation = 0
        else:
            mean_total = total / len(self.week_performances)
            self.standard_deviation = math.sqrt(mean_total) / mean

    def update_average_performance(self, performance):
        self.average_performance = float(performance)

    def update_week_performances(self, week_performance):
        self.week_performances.append(float(week_performance))

    def parse_percent(self, data):
        return float(data.strip("%")) / 100
