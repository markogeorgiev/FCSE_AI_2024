import bisect
from constraint import *


def constraint_function(zamara_free, simona_free, pero_free, sostanok):
    simona = (13, 14, 16, 19)
    zamara = (14, 15, 18)
    peropropelero = (12, 13, 16, 17, 18, 19)

    if sostanok not in simona or simona_free == 0:
        return False
    if sostanok not in peropropelero and pero_free == 1:
        return False
    if sostanok not in zamara and zamara_free == 1:
        return False

    return pero_free + zamara_free >= 1

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", [12, 13, 14, 15, 16, 17, 18, 19])
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(constraint_function,
                          ("Marija_prisustvo", "Simona_prisustvo", "Petar_prisustvo", "vreme_sostanok"))

    # ----------------------------------------------------

    solutions = problem.getSolutions()

    for solution in solutions:
        reordered_solution = {'Simona_prisustvo': solution['Simona_prisustvo'],
                              'Marija_prisustvo': solution['Marija_prisustvo'],
                              'Petar_prisustvo': solution['Petar_prisustvo'],
                              'vreme_sostanok': solution['vreme_sostanok']}
        print(reordered_solution)

