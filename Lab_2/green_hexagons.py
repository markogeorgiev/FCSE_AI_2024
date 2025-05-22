import math

from searching_framework import *


class GreenHexagons(Problem):
    def __init__(self, initial, allowed):
        super().__init__(initial)
        self.allowed = allowed

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def successor(self, state):
        # state -> (person, house)
        # state ->((px,py), (hx,hy,hd))
        successors = dict()

        person_x, person_y = state[0]
        new_house = self.make_new_house(state[1])

        # up-1
        new_person = person_x, person_y + 1
        if self.person_fits(new_person, new_house):
            successors["Gore 1"] = (new_person, new_house)
        # up-2
        new_person = person_x, person_y + 2
        if self.person_fits(new_person, new_house):
            successors["Gore 2"] = (new_person, new_house)
        # up-right-1
        new_person = person_x + 1, person_y + 1
        if self.person_fits(new_person, new_house):
            successors["Gore-desno 1"] = (new_person, new_house)
        # up-right-2
        new_person = person_x + 2, person_y + 2
        if self.person_fits(new_person, new_house):
            successors["Gore-desno 2"] = (new_person, new_house)
        # up-left-1
        new_person = person_x - 1, person_y + 1
        if self.person_fits(new_person, new_house):
            successors["Gore-levo 1"] = (new_person, new_house)
        # up-left-2
        new_person = person_x - 2, person_y + 2
        if self.person_fits(new_person, new_house):
            successors["Gore-levo 2"] = (new_person, new_house)
        # no-move
        successors["Stoj"] = (state[0], new_house)
        # print(successors)
        return successors

    def h(self, node):
        px, py = node.state[0]
        hx, hy, hd = node.state[1]
        return math.sqrt((px + hx) * (px + hx) + (py + hy) * (py + hy))/66

    def person_fits(self, person, house):
        return person in self.allowed or (person[0] == house[0] and person[1] == house[1])

    def make_new_house(self, curr_house):
        curr_house_x, curr_house_y, curr_house_d = curr_house

        if curr_house_d == "levo":
            if curr_house_x - 1 >= 0:
                return curr_house_x - 1, curr_house_y, curr_house_d
            else:
                return curr_house_x + 1, curr_house_y, "desno"
        if curr_house_d == "desno":
            if curr_house_x + 1 < 5:
                return curr_house_x + 1, curr_house_y, curr_house_d
            else:
                return curr_house_x - 1, curr_house_y, "levo"

    def goal_test(self, state):
        hx, hy, hd = state[1]
        #print(state[0], (hx, hy))
        return state[0] == (hx, hy)


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]
    # your code here
    person = tuple(map(int, input().split(",")))
    houseMD = tuple(map(int, input().split(",")))
    direction = input()

    house = houseMD[0], houseMD[1], direction
    initial = person, house

    greenHexagons = GreenHexagons(initial, allowed)
    solution = astar_search(greenHexagons)

    if solution is not None:
        print(solution.solution())
    else:
        print('No solution!')
