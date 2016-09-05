import NFLForumlaOne, NFLFormulaTwo

def fitness_formula_factory(num):
    if num == 1:
        return NFLForumlaOne.NFLFormulaOne
    elif num == 2:
        return NFLFormulaTwo.NFLFormulaTwo