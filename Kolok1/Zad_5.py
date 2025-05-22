from constraint import *


# def constraint_function(variables):


def placeholder(*args):
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    num_AI = int(input())
    num_ML = int(input())
    num_R = int(input())
    num_BI = int(input())

    AI_lectures_domain = ["Mon_11", "Mon_12",
                          "Wed_11", "Wed_12",
                          "Fri_11", "Fri_12"]

    ML_lectures_domain = ["Mon_12", "Mon_13", "Mon_15",
                          "Wed_12", "Wed_13", "Wed_15",
                          "Fri_11", "Fri_12", "Fri_15"]

    R_lectures_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15",
                         "Wed_10", "Wed_11", "Wed_12", "Wed_13", "Wed_14", "Wed_15",
                         "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]

    BI_lectures_domain = ["Mon_10", "Mon_11",
                          "Wed_10", "Wed_11",
                          "Fri_10", "Fri_11"]

    AI_exercises_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13",
                           "Thu_10", "Thu_11", "Thu_12", "Thu_13"]

    ML_exercises_domain = ["Tue_11", "Tue_13", "Tue_14",
                           "Thu_11", "Thu_13", "Thu_14"]

    BI_exercises_domain = ["Tue_10", "Tue_11",
                           "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------

    all_variables = list()

    AI_lectures = ([f"AI_cas_{i}" for i in range(1, num_AI + 1)])
    ML_lectures = ([f"ML_cas_{i}" for i in range(1, num_ML + 1)])
    R_lectures = ([f"R_cas_{i}" for i in range(1, num_R + 1)])
    BI_lectures = ([f"BI_cas_{i}" for i in range(1, num_BI + 1)])

    all_variables.extend(AI_lectures)
    all_variables.extend(ML_lectures)
    all_variables.extend(R_lectures)
    all_variables.extend(BI_lectures)

    problem.addVariable(AI_lectures, AI_lectures_domain)
    problem.addVariables(ML_lectures, ML_lectures_domain)
    problem.addVariables(R_lectures, R_lectures_domain)
    problem.addVariables(BI_lectures, BI_lectures_domain)

    problem.addVariable("AI_vezbi", AI_exercises_domain)
    problem.addVariable("ML_vezbi", ML_exercises_domain)
    problem.addVariable("BI_vezbi", BI_exercises_domain)

    all_variables.extend(["AI_vezbi", "ML_vezbi", "BI_vezbi"])



    # print(variables)
    # ---Tuka dodadete gi ogranichuvanjata----------------


    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)
