def read_input(input):
    data = []
    moves = ""
    with open(input, "r") as f:
        first_part = True
        for line in f.readlines():
            if line == '\n':
                first_part = False
                continue
            if first_part:
                row = []
                for i in line.rstrip("\n"):
                    row.append(i)
                data.append(row)
            else:
                moves += line.rstrip("\n")
    return data, moves


def get_pos(state):
    for y, row in enumerate(state):
        for x, v in enumerate(row):
            if v == '@':
                return (x, y)


def pretty_print(state):
    for row in state:
        print()
        for val in row:
            print(val, end='')


data, moves = read_input("input")
move_dict = {'^': (0, -1), '>': (1, 0), '<': (-1, 0), 'v': (0, 1)}

print(data)
print(moves)
state = data
rx, ry = get_pos(state)
for move in moves:

    dx, dy = move_dict[move]
    next_val = state[ry+dy][rx+dx]
    print(move, next_val)
    if next_val == '.':  # no obstacle, just move
        state[ry][rx] = '.'
        rx = rx+dx
        ry = ry+dy
        state[ry][rx] = '@'
    elif next_val == 'O':
        nx = rx
        ny = ry
        while next_val != '#':
            nx += dx
            ny += dy
            next_val = state[ny][nx]
            if next_val == '.':
                state[ny][nx] = 'O'
                state[ry][rx] = '.'
                rx = rx+dx
                ry = ry+dy
                state[ry][rx] = '@'

                break

pretty_print(state)

total = 0
for j, row in enumerate(state):
    for i, v in enumerate(row):
        if v == 'O':
            total += 100 * j + i
print(total)
