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
        self.weighted_moving_average = None
        self.special_stat = None
        self.wins = None

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

    def calculate_weighted_moving_average(self):
        performance_sum = 0
        for wp in self.week_performances[0:-1]:
            performance_sum += wp
        if len(self.week_performances[0:-1]) != 0:
            moving_average = performance_sum/len(self.week_performances[0:-1])
            weighted_moving_average = (moving_average + self.week_performances[-1]) / 2
            self.weighted_moving_average = weighted_moving_average

    def update_average_performance(self, performance):
        self.average_performance = float(performance)

    def update_wins(self, wins):
        self.wins = int(wins)

    def update_week_performances(self, week_performance):
        self.week_performances.append(float(week_performance))

    def parse_percent(self, data):
        return float(data.strip("%")) / 100
