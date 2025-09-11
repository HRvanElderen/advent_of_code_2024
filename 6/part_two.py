

def read_input(input):
    data = []
    with open(input, "r") as f:
        for line in f.readlines():
            row = []
            for i in line.rstrip("\n"):
                row.append(i)
            data.append(row)
    return data


def move(pos, direction):
    x, y = pos
    if direction == 0:
        x -= 1
    elif direction == 1:
        y += 1
    elif direction == 2:
        x += 1
    else:
        y -= 1
    return x, y


def pretty_print(data, points):
    for i, row in enumerate(data):
        print("\n", end='')
        for j, val in enumerate(row):
            if (i, j) in points:
                print('x', end='')
            else:
                print(val, end='')


def pretty_print_dir(data, points, obs):
    p = set()
    for (point, direction) in points:
        p.add(point)
    for i, row in enumerate(data):
        print("\n", end='')
        for j, val in enumerate(row):
            if (i, j) in p:
                print('x', end='')
            elif (i, j) in obs:
                print('#', end='')
            else:
                print('.', end='')


def find_guard_route(data, guard_coordinates):
    direction = 0
    guard_pos = guard_coordinates
    visited_points = set()
    visited_points.add(guard_pos)
    while True:

        next_pos = move(guard_pos, direction)
        if not (0 <= next_pos[0] < len(data) and 0 <= next_pos[1] < len(data[0])):
            break
        if data[next_pos[0]][next_pos[1]] == '#':
            direction = (direction + 1) % 4
        else:
            guard_pos = next_pos
        visited_points.add(guard_pos)
    return visited_points


def find_loop(data, guard_coordinates, new_obs):
    direction = 0
    guard_pos = guard_coordinates
    visited_points = set()
    visited_points.add((guard_pos, direction))

    data[new_obs[0]][new_obs[1]] = '#'
    while True:
        next_pos = move(guard_pos, direction)
        if not (0 <= next_pos[0] < len(data) and 0 <= next_pos[1] < len(data[0])):
            data[new_obs[0]][new_obs[1]] = '.'
            return False
        if data[next_pos[0]][next_pos[1]] == '#':
            direction = (direction + 1) % 4
        else:
            guard_pos = next_pos

        if (guard_pos, direction) in visited_points:
            # pretty_print(data, visited_points)
            data[new_obs[0]][new_obs[1]] = '.'
            return True

        visited_points.add((guard_pos, direction))


def get_base_state(data):
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            if value == '^':
                return (i, j)


def main():
    input = "input.txt"
    data = read_input(input)
    guard_coordinates = get_base_state(data)
    visited_points = find_guard_route(data, guard_coordinates)

    print(len(visited_points))
    loop_count = 0
    for i, point in enumerate(visited_points):
        print(i)
        if point == guard_coordinates:
            continue

        if find_loop(data, guard_coordinates, point):
            loop_count += 1
    print("loop options: " + str(loop_count))


if __name__ == "__main__":
    main()
