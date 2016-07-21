import math

class Player:

    def __init__(self, name, team, position, salary, ppg):
        self.name = name.strip()
        self.team = team
        self.position = position
        self.salary = int(salary)
        self.ppg = float(ppg)
        self.is_team = position == "TEAM"
        self.kda = None
        self.kills = None
        self.deaths = None
        self.assists = None
        self.kill_participation = None
        self.cs_per_minute = None
        self.minutes_played = None
        self.week_performances = []
        self.average_performance = None
        self.standard_deviation = None

    def update_additional_stats(self, stats):
        self.kda = float(stats[0])
        self.kills = int(stats[1])
        self.deaths = int(stats[2])
        self.assists = int(stats[3])
        self.kill_participation = self.parse_percent(stats[4])
        self.cs_per_minute = float(stats[5])
        self.minutes_played = int(stats[6].replace(',',''))

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

    def get_minute_multiplier(self):
        if self.minutes_played > 700:
            return 1
        else:
            return (self.minutes_played / 2500) + (18 / 25)

    def get_score(self):
        try:
            if self.position == "TEAM":
                return self.ppg
            else:
                return self.get_minute_multiplier() * (self.ppg + (self.kda * self.kill_participation))
        except:
            return 0
