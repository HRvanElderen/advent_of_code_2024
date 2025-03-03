from collections import deque
import copy
from functools import cache


def read_maze(file):
    with open(file, "r") as f:
        maze = []
        for line in f.read().splitlines():
            row = []
            for i in line:
                row.append(i)
            maze.append(row)
    return maze


def get_start(maze):
    for i, row in enumerate(maze):
        for j, item in enumerate(row):
            if item == "S":
                return i, j


def get_moves(maze, state):
    moves = []
    x, y = state
    for pos in [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]:
        x, y = pos
        if maze[x][y] == "." or maze[x][y] == "E":
            moves.append(pos)
    return moves


def get_cheat_moves(maze, state):
    moves = []
    x, y = state

    if (
        x + 2 < len(maze)
        and maze[x + 1][y] == "#"
        and (maze[x + 2][y] == "." or maze[x + 2][y] == "E")
    ):
        moves.append((x + 2, y))
    if (
        x - 2 > 0
        and maze[x - 1][y] == "#"
        and (maze[x - 2][y] == "." or maze[x - 2][y] == "E")
    ):
        moves.append((x - 2, y))
    if (
        y + 2 < len(maze[0])
        and maze[x][y + 1] == "#"
        and (maze[x][y + 2] == "." or maze[x][y + 2] == "E")
    ):
        moves.append((x, y + 2))
    if (
        y - 2 > 0
        and maze[x][y - 1] == "#"
        and (maze[x][y - 2] == "." or maze[x][y - 2] == "E")
    ):
        moves.append((x, y - 2))
    return moves


maze = read_maze("maze.txt")


def bfs(maze):
    start = get_start(maze)
    visited = {start: None}
    queue = deque([(start, 0)])
    while queue:
        pos, length = queue.popleft()
        x, y = pos
        if maze[x][y] == "E":
            shortest_path = []
            while pos:
                shortest_path.append(pos)
                pos = visited[pos]
            return len(shortest_path)

        for neighbour in get_moves(maze, pos):
            if neighbour not in visited:
                visited[neighbour] = pos
                queue.append((neighbour, length + 1))
    return length


length = bfs(maze)
print("base length:" + str(length))
total_cheats = dict()
for i in range(1, len(maze) - 1):
    for j in range(1, len(maze[0]) - 1):
        if maze[i][j] == "#":
            new_maze = copy.deepcopy(maze)
            new_maze[i][j] = "."
            path_len = bfs(new_maze)
            if path_len < length:
                try:
                    total_cheats[length - path_len] += 1
                except:
                    total_cheats[length - path_len] = 1

print(total_cheats)


# print(bfs_cheat(maze))
total = 0
for i in total_cheats.keys():
    if i >= 100:
        total += total_cheats[i]

print(total)
