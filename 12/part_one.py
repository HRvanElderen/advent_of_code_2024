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


def in_area(areas, i, j):
    for area in areas:
        if (i, j) in area:
            return True
    return False


def get_area(new_area, data, start, val):

    new_neighbours = neighbour_set(start) - new_area
    for x, y in new_neighbours:
        if 0 <= x < len(data[0]) and 0 <= y < len(data) and data[x][y] == val:
            new_area.add((x, y))
            new_area | get_area(new_area, data, (x, y), val)

    return new_area


data = read_input("input")

areas = []

for i, row in enumerate(data):
    for j, v in enumerate(row):
        if in_area(areas, i, j):
            continue
        else:
            new_area = set()
            new_area.add((i, j))
            new_area | get_area(new_area, data, (i, j), v)
            areas.append(new_area)


total_cost = 0

for area in areas:
    field_fence = 0
    for point in area:
        field_fence += len(neighbour_set(point) - area)
    total_cost += field_fence * len(area)

print(total_cost)
