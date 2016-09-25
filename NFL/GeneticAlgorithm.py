from __future__ import division

from NFL_Lineup_Generator import NFLLineupGenerator
from fitness_formulas.NFLFormulaFactory import fitness_formula_factory
from NFL_Lineup_Sort import sort_lineup
from constants import GET_ITERABLE_VALID_LINEUP
from Logger import get_logger

logger = get_logger()


class GeneticAlgorithm:

    def __init__(self, lineup_generator, formula_num):
        self.lineup_generator = lineup_generator
        self.ff = fitness_formula_factory(formula_num)

    def fitness(self, lineup):
        if not NFLLineupGenerator.lineup_under_salary_cap(lineup):
            return 0
        else:
            return self.ff(lineup, self.lineup_generator.player_holder)

    def run(self, generations, lineups=None, starting_lineup=None):
        if generations == 0:
            return self.get_top_lineup(lineups)
        elif not lineups:
            lineups = self.get_all_random()
            if starting_lineup:
                lineups[0] = starting_lineup

        num_valid = self.num_of_valid_lineups(lineups)
        if num_valid >= 2:
            lineups = self.mate_top_two(lineups)
        elif num_valid == 1:
            lineups = self.mate_top_one(lineups)
        else:
            lineups = self.get_all_random()
        return self.run(generations-1, lineups)

    def get_offspring(self, first, second=None):
        if second is None:
            second = self.lineup_generator.get_random_valid_lineup()
        new_lineups = []
        new_lineups.append(first)
        for position in GET_ITERABLE_VALID_LINEUP():
            new_lineups.append(self.lineup_generator.replace_player(first, second, position))
        new_lineups.append(self.lineup_generator.merge_lineups(first, second, 55))
        new_lineups.append(self.lineup_generator.merge_lineups(first, second, 60))
        new_lineups.append(self.lineup_generator.merge_lineups(first, second, 65))
        new_lineups.append(self.lineup_generator.merge_lineups(first, second, 70))
        new_lineups.append(self.lineup_generator.merge_lineups(first, second, 40, random=True))
        new_lineups.append(self.lineup_generator.merge_lineups(first, second, 35, random=True))
        new_lineups.append(self.lineup_generator.merge_lineups(first, second, 30, random=True))
        new_lineups.append(self.lineup_generator.merge_lineups(first, second, 25, random=True))
        new_lineups.append(self.lineup_generator.merge_lineups(first, second, 20, random=True))
        new_lineups.append(self.lineup_generator.merge_lineups(first, second, 10, random=True))
        return new_lineups

    def get_top_lineup(self, lineup):
        best = None
        for l in lineup:
            score = self.fitness(l)
            if best is None:
                best = [l, score]
            elif score > best[1]:
                best = [l, score]
        return best[0]

    def print_lineup(self, lineup, games=True):
        try:
            lineup = sort_lineup(lineup)
            logger.info("     {}               {}   {}   {}   {}      {}".format("Name", "Position", "Team", "Salary", "PPG", "Projected Points"))
            for p in lineup:
                logger.info("     {:18s} {:10s} {:4s}   {:6d}   {:5.3f}     {:5.3f}".format(p.name, p.position, p.team.upper(), p.salary, p.ppg, 0 if p.projected_points is None else p.projected_points))
            logger.info("     Team fitness: {}".format(self.fitness(lineup)))
            logger.info("     Team salary: {}".format(sum(int(x.salary) for x in lineup)))
            logger.info("")
            if games:
                logger.info("     Games:")
                for g in self.lineup_generator.player_holder.games:
                    logger.info("     {} vs {}".format(g[0], g[1]))
        except:
            logger.error("This player is missing data: {}".format(p.name))


    def mate_top_two(self, lineups):
        first, second = None, None
        for l in lineups:
            score = self.fitness(l)
            if first is None:
                first = [l, score]
            elif second is None:
                second = [l, score]
            elif score > first[1]:
                second = [first[0], first[1]]
                first = [l, score]
            elif score > second[1]:
                second = [l, score]
        return self.get_offspring(first[0], second[0])


    def mate_top_one(self, lineups):
        first = None
        for l in lineups:
            score = self.fitness(l)
            if first is None:
                first = [l, score]
            elif score > first[1]:
                first = [l, score]
        return self.get_offspring(first[0])

    def get_all_random(self):
        lineups = []
        for _ in range(0, 20):
            lineups.append(self.lineup_generator.get_random_valid_lineup())
        return lineups

    def num_of_valid_lineups(self, lineups):
        total = 0
        for l in lineups:
            if NFLLineupGenerator.lineup_under_salary_cap(l):
                total += 1
        return total
