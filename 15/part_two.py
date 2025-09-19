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


def any_blocked(state, nx, ny, dx, dy):
    if state[ny][nx] == '#':
        return True
    if state[ny][nx] == '[':
        return (any_blocked(state, nx+dx, ny+dy, dx,
                            dy) or any_blocked(state, nx+dx+1, ny+dy, dx, dy))
    if state[ny][nx] == ']':
        return (any_blocked(state, nx+dx, ny+dy, dx,
                            dy) or any_blocked(state, nx+dx-1, ny+dy, dx, dy))
    return False


def affected_boxes(state, nx, ny, dx, dy):
    if state[ny+dy][nx+dx] == '[':
        return affected_boxes(state, nx+dx, ny+dy, dx,
                              dy) | affected_boxes(state, nx+dx+1, ny+dy, dx, dy) | set([(nx+dx, ny+dy), (nx+dx+1, ny+dy)])
    if state[ny+dy][nx+dx] == ']':
        return affected_boxes(state, nx+dx, ny+dy, dx,
                              dy) | affected_boxes(state, nx+dx-1, ny+dy, dx, dy) | set([(nx+dx, ny+dy), (nx+dx-1, ny+dy)])
    return set()


def widen_map(data):
    new_map = []
    for row in data:
        new_row = []
        for val in row:
            if val == '#':
                new_row += ['#', '#']
            elif val == 'O':
                new_row += ['[', ']']
            elif val == '.':
                new_row += ['.', '.']
            elif val == '@':
                new_row += ['@', '.']
        new_map.append(new_row)
    return new_map


data, moves = read_input("input")
move_dict = {'^': (0, -1), '>': (1, 0), '<': (-1, 0), 'v': (0, 1)}


state = widen_map(data)

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
    elif next_val == '[' or next_val == ']':
        if dy != 0:  # up and down
            if any_blocked(state, rx+dx, ry+dy, dx, dy):
                print("blocked")
                continue
            box_coords = list(affected_boxes(state, rx, ry, dx, dy))
            if dy == -1:
                box_coords.sort(key=lambda tup: tup[1])
            else:
                box_coords.sort(key=lambda tup: tup[1], reverse=True)
            print(box_coords)
            for x, y in box_coords:
                state[y+dy][x+dx] = state[y][x]
                state[y][x] = '.'
            state[ry][rx] = '.'
            rx = rx+dx
            ry = ry+dy
            state[ry][rx] = '@'
        else:  # left and right
            nx = rx
            ny = ry
            points = []
            while next_val != '#':
                points.append((nx, ny))
                nx += dx
                ny += dy
                next_val = state[ny][nx]
                if next_val == '.':
                    for nx, ny in reversed(points):
                        state[ny+dy][nx+dx] = state[ny][nx]
                    state[ry][rx] = '.'
                    rx = rx+dx
                    ry = ry+dy
                    state[ry][rx] = '@'
                    break

pretty_print(state)

total = 0
for j, row in enumerate(state):
    for i, v in enumerate(row):
        if v == '[':
            total += 100 * j + i
print(total)
