from __future__ import division
from LineupGenerator import LineupGenerator

class LCSFormulaOne:



    @staticmethod
    def lcs_lineup_fitness(lineup):
        if not LineupGenerator.lineup_under_salary_cap(lineup):
            return 0
        else:
            fitness = LCSFormulaOne.get_lineup_player_scores(lineup)
            multipliers = LCSFormulaOne.get_multipliers(lineup)
            team_multiplier, salary_multiplier = multipliers[0], multipliers[1]
            return fitness * team_multiplier

    @staticmethod
    def get_lineup_player_scores(lineup):
        fitness = 0
        for p in lineup:
            fitness += LCSFormulaOne.get_player_score(p)
        return fitness

    @staticmethod
    def get_multipliers(lineup):
        total_salary = 0
        teams = []
        for p in lineup:
            total_salary += int(p.salary)
            if p.position != "TEAM":
                teams.append(p.team)
        most_per_team = max([teams.count(x) for x in teams])
        multipliers = [LCSFormulaOne.get_players_per_team_multiplier(most_per_team), LCSFormulaOne.get_salary_multiplier(total_salary)]
        return multipliers

    @staticmethod
    def get_players_per_team_multiplier(most_per_team):
        if most_per_team <= 4:
            return 1
        else:
            return 0

    @staticmethod
    def get_salary_multiplier(total_salary):
        if total_salary < 49000:
            return 0.975
        else:
            return (total_salary / 20000) - 1.5

    @staticmethod
    def get_player_score(player):
        try:
            return player.ppg
        except:
            return player.ppg