from constraint import *


class NonSameConstraint(Constraint):
    def __init__(self, *args):
        super().__init__(*args)

    def satisfied(self, assignment):
        nums = set()
        for var in assignment:
            value = assignment[var]
            if value in nums:
                return False
            else:
                nums.add(value)
        return True

if __name__ == '__main__':
    problem = Problem()

    variables = list()

    n = 4

    for x in range(1, n + 1):
        for y in range(1, n + 1):
            variables.append((x, y))

   # print(variables)

    domain = [1, 2, 3, 4]

    problem.addVariables(variables, domain)

    # AS INPUT::  (1,1),(1,2,(1,3),(1,4)
    # TRANSLATED:: 1      1     1   1
    for x in range(1, n + 1):
        row = [(x, y) for y in range(1, n + 1)]
        problem.addConstraint(NonSameConstraint, row)

        # Add column constraints
    for y in range(1, n + 1):
        col = [(x, y) for x in range(1, n + 1)]
        problem.addConstraint(NonSameConstraint, col)

    problem.addConstraint(lambda val1, val2: val1 > val2, [(4, 1), (4, 2)])
    problem.addConstraint(lambda val1, val2: val1 > val2, [(4, 3), (3, 3)])
    problem.addConstraint(lambda val1, val2: val1 > val2, [(4, 4), (4, 3)])
    problem.addConstraint(lambda val1, val2: val1 > val2, [(4, 4), (3, 4)])

    problem.addConstraint(lambda val1, val2: val1 > val2, [(3, 1), (4, 1)])
    problem.addConstraint(lambda val1, val2: val1 > val2, [(3, 2), (4, 2)])
    problem.addConstraint(lambda val1, val2: val1 > val2, [(3, 2), (3, 1)])
    problem.addConstraint(lambda val1, val2: val1 > val2, [(3, 2), (3, 4)])

    problem.addConstraint(lambda val1, val2: val1 > val2, [(2, 2), (2, 1)])
    problem.addConstraint(lambda val1, val2: val1 > val2, [(2, 2), (1, 2)])
    problem.addConstraint(lambda val1, val2: val1 > val2, [(2, 3), (2, 4)])
    problem.addConstraint(lambda val1, val2: val1 > val2, [(2, 3), (1, 3)])

    problem.addConstraint(lambda val1, val2: val1 > val2, [(1, 1), (1, 2)])
    problem.addConstraint(lambda val1, val2: val1 > val2, [(1, 1), (2, 1)])
    problem.addConstraint(lambda val1, val2: val1 > val2, [(1, 4), (1, 3)])
    problem.addConstraint(lambda val1, val2: val1 > val2, [(1, 4), (2, 4)])

    sols = problem.getSolution()
    if sols is not None:
        print(sols)
    else:
        print('No solutions')