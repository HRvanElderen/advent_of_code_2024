from collections import deque


def read_input(input):
    data = []
    with open(input, "r") as f:
        for line in f.readlines():
            row = []
            for i in line.rstrip("\n"):
                row.append(i)
            data.append(row)
    return data


def get_start(maze):
    for i, row in enumerate(maze):
        for j, item in enumerate(row):
            if item == "S":
                return i, j


def get_end(maze):
    for i, row in enumerate(maze):
        for j, item in enumerate(row):
            if item == "E":
                return i, j


def get_moves(maze, state):
    moves = []
    x, y = state
    for pos, d in [((x + 1, y), 'Z'), ((x, y - 1), 'W'), ((x - 1, y), 'N'), ((x, y + 1), 'E')]:
        x, y = pos
        if maze[x][y] == "." or maze[x][y] == "E":
            moves.append((pos, d))
    return moves


def pretty_print(maze, path):
    for x, row in enumerate(maze):
        print("")
        for y, val in enumerate(row):
            if (x, y) not in path:
                print(val, end='')
            else:
                print("*", end='')


def h(pos, goal):
    return abs(pos[0]-goal[0]) + abs(pos[1]-goal[1])


def a_star(start, goal, maze):
    start_state = (start, 'E')
    open_set = set()
    open_set.add(start_state)
    came_from = dict()

    g_score = dict()
    g_score[start_state] = 0

    f_score = dict()
    f_score[start_state] = h(start, goal)
    print(open_set)
    while open_set:
        curr_state = min(f_score, key=f_score.get)
        cp, cd = curr_state

        open_set.remove(curr_state)

        if cp == goal:
            return g_score[curr_state]

        for neighbour, nd in get_moves(maze, cp):
            if cd == nd:
                tg = g_score[curr_state] + 1
            else:
                tg = g_score[curr_state] + 1001

            if (neighbour, nd) not in g_score.keys():
                g_score[(neighbour, nd)] = 99999999
            if tg < g_score[(neighbour, nd)]:
                came_from[(neighbour, nd)] = cp
                g_score[(neighbour, nd)] = tg
                f_score[(neighbour, nd)] = tg + h(neighbour, goal)
                if (neighbour, nd) not in open_set:
                    open_set.add((neighbour, nd))
        g_score.pop(curr_state, None)
        f_score.pop(curr_state, None)


maze = read_input("input")
s = get_start(maze)
e = get_end(maze)
length = a_star(s, e, maze)
print(length)
