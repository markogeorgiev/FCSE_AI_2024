from constraint import *


def most_4(*args):
    topics = dict()

    for arg in args:
        if arg not in topics.keys():
            topics[arg] = 1
        else:
            topics[arg] += 1

    for topic in topics:
        if topics[topic] > 4:
            return False

    return True



if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite

    domain = [f'T{i + 1}' for i in range(num)]
    variables = [f'{paper} ({papers[paper]})' for paper in papers]

    topics = ['NLP', 'ML', 'AI']

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata

    problem.addConstraint(most_4, tuple(variables))

    for topic in topics:
        lectures = list()
        for paper in variables:
            if paper == topic:
                print(papers[paper], paper)
                lectures.append(paper)
        if len(lectures) <= 4:
            problem.addConstraint(lambda *timeslots: len(set(timeslots)) == 1, lectures)
        lectures.clear()

    result = problem.getSolution()

    # Tuka dodadete go kodot za pechatenje
    print(result)


