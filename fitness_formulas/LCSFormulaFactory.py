from fitness_formulas import LCSFormulaOne, LCSFormulaTwo, LCSFormulaThree, LCSFormulaFour

def fitness_formula_factory(num):
    if num == 1:
        return LCSFormulaOne.LCSFormulaOne
    elif num == 2:
        return LCSFormulaTwo.LCSFormulaTwo
    elif num == 3:
        return LCSFormulaThree.LCSFormulaThree
    elif num == 4:
        return LCSFormulaFour.LCSFormulaFour