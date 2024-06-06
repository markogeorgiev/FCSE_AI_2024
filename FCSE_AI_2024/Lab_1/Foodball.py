from searching_framework import *


class Foodball(Problem):
    def __init__(self, initial):
        super().__init__(initial)
        self.forbidden = list()
        self.forbidden.append((3, 3))
        self.forbidden.append((5, 4))
        self.goal_area = list()
        self.goal_area.append((7, 2))
        self.goal_area.append((7, 3))


    def successor(self, state):
        # state: (player, ball)
        #       ((player_x,player_y), (ball_x, ball_y))
        successors = dict()

        player, ball = state
        player_x, player_y = player
        ball_x, ball_y = ball

        # player up
        new_player = (player_x, player_y + 1)
        new_ball = (ball_x, ball_y + 1)
        if self.fits(new_player):
            if ball_x == new_player[0] and ball_y == new_player[1]:
                if self.ball_fits(new_ball):
                    successors['Turni topka gore'] = new_player, new_ball
            else:
                successors['Pomesti coveche gore'] = new_player, ball

        # player down
        new_player = (player_x, player_y - 1)
        new_ball = (ball_x, ball_y - 1)
        if self.fits(new_player):
            if ball_x == new_player[0] and ball_y == new_player[1]:
                if self.ball_fits(new_ball):
                    successors['Turni topka dolu'] = new_player, new_ball
            else:
                successors['Pomesti coveche dolu'] = (new_player, ball)

        # player right
        new_player = (player_x + 1, player_y)
        new_ball = (ball_x + 1, ball_y)
        if self.fits(new_player):
            if ball_x == new_player[0] and ball_y == new_player[1]:
                if self.ball_fits(new_ball):
                    successors['Turni topka desno'] = new_player, new_ball
            else:
                successors['Pomesti coveche desno'] = (new_player, ball)

        # player up-right
        new_player = (player_x + 1, player_y + 1)
        new_ball = (ball_x + 1, ball_y + 1)
        if self.fits(new_player):
            if ball_x == new_player[0] and ball_y == new_player[1]:
                if self.ball_fits(new_ball):
                    successors['Turni topka gore-desno'] = new_player, new_ball
            else:
                successors['Pomesti coveche gore-desno'] = (new_player, ball)

        # player down-right
        new_player = (player_x + 1, player_y - 1)
        new_ball = (ball_x + 1, ball_y - 1)
        if self.fits(new_player):
            if ball_x == new_player[0] and ball_y == new_player[1]:
                if self.ball_fits(new_ball):
                    successors['Turni topka dolu-desno'] = new_player, new_ball
            else:
                successors['Pomesti coveche dolu-desno'] = new_player, ball

        return successors

    def fits(self, pos):
        #print(pos, self.forbidden)
        return 0 <= pos[0] < 8 and 0 <= pos[1] < 6 \
            and pos not in self.forbidden

    def ball_fits(self, pos):
        expanded_forbidden = []

        for x, y in self.forbidden:
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if (i, j) != (x, y):
                        expanded_forbidden.append((i, j))

        expanded_forbidden = list(set(expanded_forbidden))

        return 0 <= pos[0] < 8 and 0 <= pos[1] < 6 \
            and pos not in expanded_forbidden



    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def value(self):
        return 1

    def goal_test(self, state):
        return state[1] in self.goal_area


if __name__ == '__main__':
    player = tuple(map(int, input().split(",")))
    ball = tuple(map(int, input().split(",")))

    initial = player, ball

    football = Foodball(initial)

    if depth_first_graph_search(football) is None:
        print('No solution!')
    else:
        print(depth_first_graph_search(football).solution())
