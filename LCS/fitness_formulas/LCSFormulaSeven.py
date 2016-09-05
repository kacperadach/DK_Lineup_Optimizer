from __future__ import division

from LCS.LineupGenerator import LineupGenerator
from LCS.fitness_formulas import LCSFormulaOne, LCSFormulaTwo, LCSFormulaThree, LCSFormulaFour, LCSFormulaFive, LCSFormulaSix

# all formulas


TEAM_BLACKLIST = ()
PLAYER_BLACKLIST = ()


def LCSFormulaSeven(lineup, player_holder):
    if not LineupGenerator.lineup_under_salary_cap(lineup):
        return 0
    else:
        formula_sum = sum([LCSFormulaOne.LCSFormulaOne(lineup, player_holder),
                           LCSFormulaTwo.LCSFormulaTwo(lineup, player_holder),
                           LCSFormulaThree.LCSFormulaThree(lineup, player_holder),
                           LCSFormulaFour.LCSFormulaFour(lineup, player_holder),
                           LCSFormulaFive.LCSFormulaFive(lineup, player_holder),
                           LCSFormulaSix.LCSFormulaSix(lineup, player_holder)])
        average_val = formula_sum / 6
        return average_val



