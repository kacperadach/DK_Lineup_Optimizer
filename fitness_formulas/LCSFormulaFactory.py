from fitness_formulas import LCSFormulaOne, LCSFormulaTwo

def fitness_formula_factory(num):
    if num == 1:
        return LCSFormulaOne.LCSFormulaOne
    elif num == 2:
        return LCSFormulaTwo.LCSFormulaTwo