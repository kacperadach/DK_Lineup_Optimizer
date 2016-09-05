import NFLForumlaOne, NFLFormulaTwo, NFLFormulaThree

def fitness_formula_factory(num):
    if num == 1:
        return NFLForumlaOne.NFLFormulaOne
    elif num == 2:
        return NFLFormulaTwo.NFLFormulaTwo
    elif num == 3:
        return NFLFormulaThree.NFLFormulaThree