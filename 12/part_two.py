def read_input(input):
    data = []
    with open(input, "r") as f:
        for line in f.readlines():
            row = []
            for i in line.rstrip("\n"):
                row.append(i)
            data.append(row)
    return data


def get_neighbours(i, j):
    return [(i, j-1), (i-1, j), (i+1, j), (i, j+1)]


def neighbour_set(point):
    x, y = point
    return {(x+1, y), (x-1, y), (x, y+1), (x, y-1)}


def in_area(areas, x, y):
    for area in areas:
        if (x, y) in area:
            return True
    return False


def get_area(new_area, data, start, val):
    new_neighbours = neighbour_set(start) - new_area
    for x, y in new_neighbours:
        if 0 <= x < len(data[0]) and 0 <= y < len(data) and data[y][x] == val:
            new_area.add((x, y))
            new_area | get_area(new_area, data, (x, y), val)

    return new_area


def point_corners(area, point):
    corners = set()
    x, y = point
    for dx, dy in [(x+1, y), (x+1, y+1), (x, y), (x, y+1)]:
        square = {(dx-1, dy), (dx-1, dy-1), (dx, dy), (dx, dy-1)}
        dif = square - area

        if len(square - area) % 2 == 1:
            corners.add(frozenset(square))
        elif len(dif) == 2:
            dif_list = list(dif)
            if abs(dif_list[0][0] - dif_list[1][0]) == 1 and abs(dif_list[0][1] - dif_list[1][1]) == 1:
                corners.add(frozenset(dif))
    return corners


data = read_input("input")

areas = []

for y, row in enumerate(data):
    for x, v in enumerate(row):
        if in_area(areas, x, y):
            continue
        else:
            new_area = set()
            new_area.add((x, y))
            new_area | get_area(new_area, data, (x, y), v)
            areas.append(new_area)


price = 0
for area in areas:
    corners = set()
    for point in area:
        corners = corners | point_corners(area, point)

    corner_count = 0

    for corner in corners:
        if len(corner) == 2:
            corner_count += 2
        else:
            corner_count += 1
    price += corner_count * len(area)


print(price)
# total_cost = 0
# print(areas)
# for area in areas:
#     field_fence = 0
#     for point in area:
#         field_fence += len(neighbour_set(point) - area)
#     total_cost += field_fence * len(area)

# print(total_cost)
