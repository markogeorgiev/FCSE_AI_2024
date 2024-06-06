from searching_framework import *


class Green_Hexagons2(Problem):
    def __init__(self, initial, allowed):
        super().__init__(initial)
        self.allowed = allowed

    def successor(self, state):
        successors = dict()
        # state -> (person, house)
        # state -> ((person_x, person_y)(house_x, house_y, house_d))

        person_x, person_y = state[0]

        new_house = self.generate_house(state[1])

        # stoj
        new_person = person_x, person_y
        successors['Stoj'] = (new_person, new_house)
        # gore-1
        new_person = person_x, person_y + 1
        if self.person_in_ok_position(new_person, new_house):
            successors['Gore 1'] = (new_person, new_house)
        # gore-2
        new_person = person_x, person_y + 2
        if self.person_in_ok_position(new_person, new_house):
            successors['Gore 2'] = (new_person, new_house)
        # gore-desno-1
        new_person = person_x + 1, person_y + 1
        if self.person_in_ok_position(new_person, new_house):
            successors['Gore-desno 1'] = (new_person, new_house)
        # gore-desno-2
        new_person = person_x + 2, person_y + 2
        if self.person_in_ok_position(new_person, new_house):
            successors['Gore-desno 2'] = (new_person, new_house)
        # gore-levo-1
        new_person = person_x - 1,  person_y + 1
        if self.person_in_ok_position(new_person, new_house):
            successors['Gore-levo 1'] = (new_person, new_house)
        # gore-levo-2
        new_person = person_x - 2, person_y + 2
        if self.person_in_ok_position(new_person, new_house):
            successors['Gore-levo 2'] = (new_person, new_house)

        return successors


    def person_in_ok_position(self, new_person, new_house):
        return (new_person in self.allowed \
                or (new_house[0] == new_person[0] and new_house[1] == new_person[1]))

    def generate_house(self, curr_house):
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

    def h(self, node):
        # state -> ((person_x, person_y)(house_x, house_y, house_d))
        px, py = node.state[0]
        hx, hy, hd = node.state[1]
        return (abs(px - hx) + abs(py - hy))/2.5

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        # ((person_x, person_y)(house_x, house_y, house_d))
        hx, hy, hd = state[1]
        return state[0] == (hx, hy)


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2),
               (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    person = tuple(map(int, input().split(",")))
    house = tuple(map(int, input().split(",")))
    house_d = input()

    # state -> ((person_x, person_y)(house_x, house_y, house_d))
    initial = (person, (house[0], house[1], house_d))

    hexagons = Green_Hexagons2(initial, allowed)

    sol = astar_search(hexagons)

    if sol is not None:
        print(sol.solution())
    else:
        print('No solution!')
