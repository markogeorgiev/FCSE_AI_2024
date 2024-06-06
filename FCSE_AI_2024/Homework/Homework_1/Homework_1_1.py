import copy

from searching_framework import *


class MultiplePackman(Problem):
    def __init__(self, initial, pallets, obstacles, bag_capacity, n, m):
        super().__init__(initial)
        self.pallets = pallets
        self.obstacles = obstacles
        self.n = n
        self.m = m
        self.bag_capacity = bag_capacity
        self.moves = {"Горе": (0, 1),
                      "Долу": (0, -1),
                      "Лево": (-1, 0),
                      "Десно": (1, 0),
                      "Стоп": (0, 0)}

    def get_taken_pallets(self, current_state):
        taken_pallets = []
        for pacman in current_state.pallets:
            taken_pallets.extend(pacman[2])
        return taken_pallets

    def is_valid_pos(self, x, y):
        return 0 <= x < n and 0 <= y < m and (x, y) not in self.obstacles and (x, y)

    def apply_move(self, move, pacman):
        px, py = pacman
        return px + move[0], py + move[1], pacman[2]

    def successor(self, state):
        successors = dict()
        # stop, stop
        # stop, up
        # stop, down
        # stop, left
        # stop, right
        # up, stop
        # up, up
        # up, down
        # up, left
        # up, right
        # down, stop
        # down, up
        # down, down
        # down, left
        # down, right
        # right, stop
        # right, up
        # right, down
        # right, left
        # right, right
        # left, stop
        # left, up
        # left, down
        # left, left
        # left, right

        # for index in range(len(pacman_list)):
        #    # for each pacman we make every move available
        #    curr_pacman = pacman_list[index]

        #    if curr_pacman[2] == self.bag_capacity:
        #        return  successors['All wait']

        #    for move in self.moves.keys():
        #        nx, ny = curr_pacman[0] + move[0], curr_pacman[1] + move[1]
        #        if self.is_valid_pos(nx, ny, curr_pacman[2]):
        #            if (nx, ny) in remaining_pallets:


        # (((pmx1,pmy1, np1),(pmx2,pmy2, np2), … , (pmxK, pmyK, npK)), [(f1x, f1y), (f2x, f2y), … , (fPx, fPy)] )
#
     #   # for i in range(pow(len(pacman_list), 5)):
     #   remaining_pallets = state[1]
     #   pacman_list = state[0]
     #   for move1 in self.moves:
     #       # Create deep_copy of remaining pallets to use for creating the new_state. If a pallet is eat remove it from deep_copy
     #       new_sate = list()
     #       # apply move1 to pacman1 and check validity of 1st pacman
     #       # if is_valid_pos move on to next for
     #       # else
     #       # check if there's a pallet in the current position, if there is eat it and add 1 to the current pacman's bag
     #       # append the pacman to new_state and enter to the next for loop
     #       for move2 in self.moves:
     #           # apply move2 to pacman2 and check validity of 2nd pacman
     #           # if is_valid_pos move on to next for
     #           # else
     #           # check if there's a pallet in the current position, if there is eat it and add 1 to the current pacman's bag
     #           # append the pacman to new_state and enter to the next for loop
     #           ...
     #           for moveK in self.moves:
     #       # apply moveK to pacmanK and check validity of Kth pacman
     #   # if is_valid_pos move on to next for
     #   # else
     #   # check if there's a pallet in the current position, if there is eat it and add 1 to the current pacman's bag
     #   # append the pacman to new_state and add to the successor dictionary
     #   # successor[f'Pacman 1: {move1}, Pacman 2: {move2}, ... Pacman K: {moveK}'] = tuple(new_state)
#
         #   remaining_pallets = state[1]
         #   pacman_list = state[0]
         #   successors = {}
#
         #   for move1 in self.moves:
         #       new_state = deepcopy(pacman_list)
         #       apply_move(move1, new_state[0])
#
         #       if is_valid_pos(new_state[0][0], new_state[0][1]):
         #           for move2 in self.moves:
         #               apply_move(move2, new_state[1])
#
         #               if is_valid_pos(new_state[1][0], new_state[1][1]):
         #                   ...
         #                   for moveK in self.moves:
         #                       apply_move(moveK, new_state[K])
#
         #                       if is_valid_pos(new_state[K][0], new_state[K][1]):
         #                           # Check for pallets and eat if present
         #                           for i in range(len(new_state)):
         #                               if (new_state[i][0], new_state[i][1]) in remaining_pallets:
         #                                   new_state[i][2] += 1
         #                                   remaining_pallets.remove((new_state[i][0], new_state[i][1]))
#
         #                           successors[f'Pacman 1: {move1}, Pacman 2: {move2}, ..., Pacman K: {moveK}'] = tuple(new_state)
#
        return successors




def goal_test(self, node):
    c_state = node.state
    num_total_pallets = 0
    for pacman in c_state:
        c_list = pacman[2]
        num_total_pallets += len(c_list)
    return num_total_pallets == len(self.pallets)


def actions(self, state):
    return self.successor(state).keys()


def result(self, state, action):
    return self.successor(state)[action]


if __name__ == '__main__':
    n = int(input())
    m = int(input())

    num_pacmans = int(input())
    pacman_bag_capacity = int(input())

    num_pallets = int(input())

    pallets = list()
    for _ in range(num_pallets):
        pallets.append(map(int, input().split(",")))

    num_obstacles = int(input())

    obstacles = list()
    for _ in range(num_obstacles):
        obstacles.append(map(int, input().split(",")))

    # (((pmx1,pmy1, np1), (pmx2,pmy2, np2), (pmx3,pmy3, np3), … , (pmxK, pmyK, npK)), [(f1x, f1y), (f2x, f2y), … , (fPx, fPy)] )
    pacman_data = list()

    # at most we have 4 pacman on the game area
    for _ in range(max(4, num_pacmans)):
        pacman_data.append((0, 0, 0))

    problem = MultiplePackman((pacman_data, pallets), pallets, obstacles, pacman_bag_capacity, n, m)
