def read_input(input):
    data = []
    with open(input, "r") as f:
        for line in f.readlines():
            row = []
            for i in line.rstrip("\n"):
                row.append(int(i))
            data.append(row)
    return data


def get_next(data, pos):
    next_locs = []
    x, y = pos
    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        if 0 <= x+dx < len(data[0]) and 0 <= y+dy < len(data) and data[x+dx][y+dy] == data[x][y] + 1:
            next_locs.append((x+dx, y+dy))
    return next_locs


def find_paths(data, pos, tops):
    x, y = pos
    if data[x][y] == 9:
        tops.add((x, y))
        return tops
    next_steps = get_next(data, pos)

    if next_steps == []:
        return tops

    sub_tot = 0
    for s in next_steps:
        tops = tops | find_paths(data, s, tops)
    return tops


data = read_input("input")

trail_heads = []

for i, row in enumerate(data):
    for j, v in enumerate(row):
        if v == 0:
            trail_heads.append((i, j))

total = 0
for h in trail_heads:
    tops = set()
    tops = find_paths(data, h, tops)
    total += len(tops)

print(total)
