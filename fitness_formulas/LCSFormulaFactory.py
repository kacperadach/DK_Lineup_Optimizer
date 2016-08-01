from fitness_formulas import LCSFormulaOne, LCSFormulaTwo, LCSFormulaThree, LCSFormulaFour, LCSFormulaFive, LCSFormulaSix, LCSFormulaSeven

def fitness_formula_factory(num):
    if num == 1:
        return LCSFormulaOne.LCSFormulaOne
    elif num == 2:
        return LCSFormulaTwo.LCSFormulaTwo
    elif num == 3:
        return LCSFormulaThree.LCSFormulaThree
    elif num == 4:
        return LCSFormulaFour.LCSFormulaFour
    elif num == 5:
        return LCSFormulaFive.LCSFormulaFive
    elif num == 6:
        return LCSFormulaSix.LCSFormulaSix
    elif num == 7:
        return LCSFormulaSeven.LCSFormulaSeven