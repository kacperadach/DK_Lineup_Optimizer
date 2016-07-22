from CSVPlayerGather import get_all_players
from LineupGenerator import LineupGenerator
from LoLPlayerHolder import LoLPlayerHolder
from GeneticAlgorithm import GeneticAlgorithm
from AdditionalStats import update_lcs_fantasy_stats

all_players = get_all_players("DKSalaries.txt")
player_holder = LoLPlayerHolder(all_players)
update_lcs_fantasy_stats(player_holder, 1, 8, "lcs_fantasy_")
lineup_gen = LineupGenerator(player_holder)
g = GeneticAlgorithm(lineup_gen, 1)
best_lineups=[]
for _ in range(0, 9):
    best_lineups.append(g.run(500))
best_lineups.sort(key=lambda x: g.fitness(x), reverse=True)
g.print_lineup(best_lineups[0])
#lineup_gen.print_players('mid')

