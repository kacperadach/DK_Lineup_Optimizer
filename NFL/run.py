from datetime import datetime

from fantasy_pros_scraper import scrape
from CSVPlayerGather import get_all_games, get_all_players, get_all_projections
from NFL_Player_Holder import NFLPlayerHolder
from NFL_Lineup_Generator import NFLLineupGenerator
from NFL.GeneticAlgorithm import GeneticAlgorithm
from Logger import get_logger

logger = get_logger()

DK_SALARY_CSV = "DKSalaries.txt"
PROJECTIONS_CSV = "fan-pros-projections.csv"


def run(fitness_formula, week=None, iterations=9, generations=500):
    scrape(week)
    start_time = datetime.now()
    logger.info("Beginning Algorithm")
    all_players = get_all_players(DK_SALARY_CSV)
    all_games = get_all_games(DK_SALARY_CSV)
    player_holder = NFLPlayerHolder(all_players, all_games)
    player_holder.update_projections(get_all_projections(PROJECTIONS_CSV))
    player_holder.remove_non_projected_players()
    lineup_gen = NFLLineupGenerator(player_holder)
    g = GeneticAlgorithm(lineup_gen, fitness_formula)
    # best_lineup = None
    # for x in range(0, iterations):
    #     logger.info("Generation {}".format(x + 1))
    #     if not best_lineup:
    #         best_lineup = g.run(generations)
    #     else:
    #         best_lineup = g.run(generations, starting_lineup=best_lineup)
    # g.print_lineup(best_lineup)
    best_lineups = []
    for x in range(0, iterations):
        logger.info("Generation {}".format(x + 1))
        best_lineups.append(g.run(generations))
    best_lineups.sort(key=lambda x: g.fitness(x), reverse=True)
    g.print_lineup(best_lineups[0])
    end_time = datetime.now()
    logger.info("Finished Algorithm, total time: {}".format(end_time-start_time))

run(4, iterations=10)