def read_input(input):
    data = []
    with open(input, "r") as f:
        for line in f.readlines():
            row = []
            for i in line.rstrip("\n"):
                row.append(i)
            data.append(row)
    return data


data = read_input("input.txt")
print(data)
x_len = len(data[0])
y_len = len(data)
antennas = dict()

for i, row in enumerate(data):
    for j, value in enumerate(row):
        if value == '.':
            continue
        if value in antennas.keys():
            antennas[value].append((i, j))
        else:
            antennas[value] = [(i, j)]

print(antennas)
antinodes = set()
for antenna, locations in antennas.items():
    i = 1
    for l1 in locations:
        for l2 in locations[i:]:
            x, y = l1
            x1, y1 = l2
            dx = x-x1
            dy = y-y1
            # if x1-dx < 0 or y1-dy < 0 or x+dx
            antinodes.add((x+dx, y+dy))
            antinodes.add((x1-dx, y1-dy))
        i += 1

total = 0
for x, y in antinodes:
    if (0 <= x < x_len and 0 <= y < y_len):
        total += 1
print(total)
