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
        self.weighted_standard_deviation = None
        self.special_stat = None

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

    def calculate_weighted_stan_dev(self):
        mean = self.average_performance
        if mean is None:
            return
        len_wp = len(self.week_performances)
        if len_wp == 0:
            self.weighted_standard_deviation = 0
        else:
            total = 0
            for x in range(0, len_wp-1):
                total += ((self.week_performances[x] - mean) * (self.week_performances[x] - mean))
            mean_total = total / (len_wp - 1)
            stan_dev = math.sqrt(mean_total) / mean
            last_performance_stdev = math.sqrt((self.week_performances[len_wp-1] - mean) * (self.week_performances[len_wp-1] - mean)) / mean
            self.weighted_standard_deviation = (last_performance_stdev + stan_dev) / 2


    def update_average_performance(self, performance):
        self.average_performance = float(performance)

    def update_week_performances(self, week_performance):
        self.week_performances.append(float(week_performance))

    def parse_percent(self, data):
        return float(data.strip("%")) / 100
