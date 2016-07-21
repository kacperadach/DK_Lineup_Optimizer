from CSVPlayerGather import CSVPlayerGather
from LineupGenerator import LineupGenerator
from LoLPlayerHolder import LoLPlayerHolder
from GeneticAlgorithm import GeneticAlgorithm, logger
from AdditionalStats import update_lcs_player_stats, update_lcs_fantasy_stats

all_players = CSVPlayerGather.get_all_players("DKSalaries_eulcs.txt")
player_holder = LoLPlayerHolder(all_players)
update_lcs_fantasy_stats(player_holder, 1, 7)
lineup_gen = LineupGenerator(player_holder)
# g = GeneticAlgorithm(lineup_gen)
# best_lineups=[]
# for _ in range(0, 9):
#     best_lineups.append(g.run(500))
# best_lineups.sort(key=lambda x: g.fitness(x), reverse=True)
# g.print_lineup(best_lineups[0])
lineup_gen.print_players('jng')

