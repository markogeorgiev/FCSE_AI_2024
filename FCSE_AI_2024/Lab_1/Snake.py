from searching_framework import *

class Snake(Problem):
    def __init__(self, initial, red_apples):
        super().__init__(initial)
        self.red_apples = red_apples

    def successor(self, state):
        # state -> (snake_head, snake_body, green_apples)
        successors = dict()

        snake_head, snake_body, green_apples = state
        # initial = ((2, 0, 'v'), ((1,0), (0,0)), green_apples)
        head_x = snake_head[0]
        head_y = snake_head[1]
        head_d = snake_head[2]

        curr_apples = list(green_apples)

        if head_d == 'v':
            # ushe dole
            new_head = (head_x, head_y - 1)
            if self.fits(head_x, head_y - 1, snake_body):
                # calculate_board(self, new_head, old_body, old_apples, new_direction)
                successors["ProdolzhiPravo"] = self.calculate_board(new_head, snake_body, curr_apples, 'v')
            # levo
            new_head = (head_x + 1, head_y)
            if self.fits(head_x + 1, head_y, snake_body):
                successors["SvrtiLevo"] = self.calculate_board(new_head, snake_body, curr_apples, '>')
            # desno
            new_head = (head_x - 1, head_y)
            if self.fits(head_x - 1, head_y, snake_body):
                successors["SvrtiDesno"] = self.calculate_board(new_head, snake_body, curr_apples, '<')

        elif head_d == '<':
            # teraj levo
            new_head = (head_x - 1, head_y)
            if self.fits(head_x - 1, head_y, snake_body):
                successors["ProdolzhiPravo"] = (
                    self.calculate_board(new_head, snake_body, curr_apples, '<'))
            # smeni desno
            new_head = (head_x, head_y + 1)
            if self.fits(head_x, head_y + 1, snake_body):
                successors["SvrtiDesno"] = self.calculate_board(new_head, snake_body, curr_apples, '^')

            # pak levo -> nadolu
            new_head = (head_x, head_y - 1)
            if self.fits(head_x, head_y - 1, snake_body):
                successors["SvrtiLevo"] = self.calculate_board(new_head, snake_body, curr_apples, 'v')


        elif head_d == '^':
            # teraj gore
            new_head = (head_x, head_y + 1)
            if self.fits(head_x, head_y + 1, snake_body):
                successors["ProdolzhiPravo"] = self.calculate_board(new_head, snake_body, curr_apples, '^')
            # smeni levo
            new_head = (head_x - 1, head_y)
            if self.fits(head_x - 1, head_y, snake_body):
                successors["SvrtiLevo"] = self.calculate_board(new_head, snake_body, curr_apples, '<')

            new_head = (head_x + 1, head_y)
            if self.fits(head_x + 1, head_y, snake_body):
                successors["SvrtiDesno"] = self.calculate_board(new_head, snake_body, curr_apples, '>')

        elif head_d == '>':
            # teraj desno
            new_head = (head_x + 1, head_y)
            if self.fits(head_x + 1, head_y, snake_body):
                successors["ProdolzhiPravo"] = self.calculate_board(new_head, snake_body, curr_apples, '>')

            # Smeni levo -> gore
            new_head = (head_x, head_y + 1)
            if self.fits(head_x, head_y + 1, snake_body):
                successors["SvrtiLevo"] = self.calculate_board(new_head, snake_body, curr_apples, '^')

            # Smeni desno -> dolu
            new_head = (head_x, head_y - 1)
            if self.fits(head_x, head_y - 1, snake_body):
                successors["SvrtiDesno"] = self.calculate_board(new_head, snake_body, curr_apples, 'v')
        # print(successors)
        return successors

    def fits(self, x, y, body):
        return 0 <= x < 10 and 0 <= y < 10 and (x, y) not in self.red_apples and (x, y) not in body

    def calculate_board(self, new_head, old_body, old_apples, new_direction):
        fix_body = list(old_body)
        fix_apples = list(old_apples)

        if new_head in old_apples:
            fix_apples.remove(new_head)
            fix_body.insert(0, new_head)
        else:
            fix_body = fix_body[:-1]
            fix_body.insert(0, new_head)
        # initial = ((2, 0, 'V'), ((1,0), (0,0)), green_apples)
        new_state = (new_head[0], new_head[1], new_direction), tuple(fix_body), tuple(fix_apples)
        # print(new_state)
        return new_state

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def value(self):
        return 1

    def goal_test(self, state):
        return len(state[2]) == 0


if __name__ == '__main__':
    red_apples = list()
    green_apples = list()

    n = int(input())
    for _ in range(n):
        line = input().split(",")
        i = int(line[0])
        j = int(line[1])
        green_apples.append((i, j))

    n = int(input())
    for _ in range(n):
        line = input().split(",")
        i = int(line[0])
        j = int(line[1])
        red_apples.append((i, j))

    # state -> (snake_head, snake_body, green_apples)
    initial = ((0, 7, 'v'), ((0, 8), (0, 9)), tuple(green_apples))
    snake = Snake(initial, tuple(red_apples))
    print(breadth_first_graph_search(snake).solution())
