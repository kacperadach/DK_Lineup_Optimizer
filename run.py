from CSVPlayerGather import get_all_players, get_all_games
from LineupGenerator import LineupGenerator
from LoLPlayerHolder import LoLPlayerHolder
from GeneticAlgorithm import GeneticAlgorithm
from AdditionalStats import update_lcs_fantasy_stats

DK_SALARY_CSV = "DKSalaries.txt"

def run(start_week, end_week, fitness_formula, iterations=9, generations=500):
    all_players = get_all_players(DK_SALARY_CSV)
    all_games = get_all_games(DK_SALARY_CSV)
    player_holder = LoLPlayerHolder(all_players, all_games)
    update_lcs_fantasy_stats(player_holder, start_week, end_week)
    lineup_gen = LineupGenerator(player_holder)
    g = GeneticAlgorithm(lineup_gen, fitness_formula)
    best_lineups=[]
    for _ in range(0, iterations):
        best_lineups.append(g.run(generations))
    best_lineups.sort(key=lambda x: g.fitness(x), reverse=True)
    g.print_lineup(best_lineups[0])

if __name__ == "__main__":
    run(1, 8, 3)

#lineup_gen.print_players('all')

