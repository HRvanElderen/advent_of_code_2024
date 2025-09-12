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


def find_paths(data, pos):
    x, y = pos
    if data[x][y] == 9:
        return 1
    next_steps = get_next(data, pos)
    # print(data[x][y], [data[x][y] for x, y in next_steps])
    if next_steps == []:
        return 0

    sub_tot = 0
    for s in next_steps:

        sub_tot += find_paths(data, s)
    return sub_tot


data = read_input("input")
print(data)

trail_heads = []

for i, row in enumerate(data):
    for j, v in enumerate(row):
        if v == 0:
            trail_heads.append((i, j))

total = 0
for h in trail_heads:
    score = find_paths(data, h)
    total += score

print(total)
