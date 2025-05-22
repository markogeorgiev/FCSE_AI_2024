from constraint import *

def at_most_4_per_slot(*args):
    tracker = dict()

    for timeslot in args:
        if timeslot not in tracker.keys():
            tracker[timeslot] = 1
        else:
            tracker[timeslot] += 1

    for val in tracker.values():
        if val > 4: return False
    return True

def same_timeslot(*arge):
    return len(set(arge)) == 1

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
    variables = [var + f" ({papers[var]})" for var in papers.keys()]
    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    print(variables)
    print(tuple(variables))
    # Tuka dodadete gi ogranichuvanjata
    problem.addConstraint(at_most_4_per_slot, tuple(variables))
    topics = tuple(set(papers.values()))

    for topic in topics:
        panels_on_topic = list()
        for panel in variables:
            if topic in panel:
                panels_on_topic.append(panel)
        if len(panels_on_topic) < 5:
            problem.addConstraint(same_timeslot, panels_on_topic)

    result = problem.getSolution()
    # Tuka dodadete go kodot za pechatenje
    for v in variables:
        print(v + ": " + result[v])
