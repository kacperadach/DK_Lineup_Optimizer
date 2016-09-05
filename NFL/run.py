from scraper import scrape
from CSVPlayerGather import get_all_games, get_all_players, get_all_projections
from NFL_Player_Holder import NFLPlayerHolder
from NFL_Lineup_Generator import NFLLineupGenerator
from constants import GET_ITERABLE_VALID_LINEUP
from NFL.GeneticAlgorithm import GeneticAlgorithm
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


DK_SALARY_CSV = "DKSalaries.txt"
PROJECTIONS_CSV = "fan-pros.csv"

def run(fitness_formula, week=1, iterations=9, generations=500):
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
    best_lineups=[]
    for x in range(0, iterations):
        logger.info("Generation {}".format(x + 1))
        best_lineups.append(g.run(generations))
    best_lineups.sort(key=lambda x: g.fitness(x), reverse=True)
    g.print_lineup(best_lineups[0])
    end_time = datetime.now()
    logger.info("Finished Algorithm, total time: {}".format(end_time-start_time))

run(4, week=1, iterations=10)