


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
    x,y = pos
    if direction == 0:
        x -= 1
    elif direction == 1:
        y += 1
    elif direction == 2:
        x += 1
    else:
        y -= 1
    return x, y

def check_obstacle(pos, obstacles, direction):
    x,y = pos
    if direction == 0 and (x-1,y) in obstacles:
        direction = 1
    elif direction == 1 and (x,y+1) in obstacles:
        direction = 2
    elif direction == 2 and (x+1,y) in obstacles:
        direction = 3
    elif direction == 3 and (x,y-1) in obstacles:
        direction = 0
    return direction

def pretty_print(data, points):
    for i, row in enumerate(data):
        print("\n", end='')
        for j, val in enumerate(row):
            if (i,j) in points:
                print('x', end='')
            else:
                print(val, end='')
            


input = "input.txt"
data = read_input(input)

print(data)
guard_coordinates = None
obstacle_coordinates = []
for i, row in enumerate(data):
    for j, value in enumerate(row):
        if value == '#':
            obstacle_coordinates.append((i,j))
        elif value == '^':
            guard_coordinates = (i,j)

print(obstacle_coordinates)
print(guard_coordinates)    
direction = 0

guard_pos = guard_coordinates
visited_points = set()
visited_points.add(guard_pos)
while True:
    direction = check_obstacle(guard_pos, obstacle_coordinates, direction)

    guard_pos = move(guard_pos, direction)
    if guard_pos[0] < 0 or guard_pos[0] >= len(data) or guard_pos[1] < 0 or guard_pos[1] >= len(data[0]):
        break
    visited_points.add(guard_pos)


print(len(visited_points))

pretty_print(data, visited_points)