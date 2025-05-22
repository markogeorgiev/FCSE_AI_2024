from searching_framework import *

class Labyrinth(Problem):
    def __init__(self, initial, obstacles, house, grid_size):
        super().__init__(initial)
        self.obstacles = obstacles
        self.house = house
        self.grid_size = grid_size


    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def successor(self, state):
        successors = dict()
        #state -> (player_x, player_y)
        player_x, player_y = state

        #desno-2
        new_player = self.move_right((player_x, player_y), 2)
        if new_player is not None:
            successors['Desno 2'] = new_player
        #desno-3
        new_player = self.move_right((player_x, player_y), 3)
        if new_player is not None:
            successors['Desno 3'] = new_player
        #gore
        new_player = player_x, player_y + 1
        if self.player_fits(new_player):
            successors['Gore'] = new_player
        #dolu
        new_player = player_x, player_y - 1
        if self.player_fits(new_player):
            successors['Dolu'] = new_player
        #levo
        new_player = player_x - 1, player_y
        if self.player_fits(new_player):
            successors['Levo'] = new_player

        return successors

    def move_right(self, curr_player, num):
        counter = 1
        for _ in range(num):
            if not self.player_fits((curr_player[0] + counter, curr_player[1])):
                return None
            counter+=1
        return curr_player[0] + num, curr_player[1]

    def h(self, node):
        player = node.state
        return (abs(player[0] - house[0]) + abs(player[1] - house[1]))/66

    def player_fits(self, curr_player):
        return curr_player not in obstacles \
            and 0 <= curr_player[0] < self.grid_size \
            and 0 <= curr_player[1] < self.grid_size


    def goal_test(self, state):
        return state == house


if __name__ == '__main__':
    n = int(input())

    k = int(input())
    obstacles = []

    for _ in range(k):
        obstacles.append(tuple(map(int, input().split(","))))

    player = tuple(map(int, input().split(",")))
    house = tuple(map(int, input().split(",")))

    initial = player

    labyrinth = Labyrinth(initial, obstacles, house, n)

    sol = astar_search(labyrinth)

    if sol is not None:
        print(sol.solution())
    else:
        print("No solution found")

