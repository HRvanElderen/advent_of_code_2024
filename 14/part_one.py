def read_input(input):
    positions = []
    velocities = []
    with open(input, "r") as f:
        for line in f.readlines():
            pos, v = line.split(" ")
            x, y = pos.strip(" p=").split(',')
            positions.append((int(x), int(y)))
            vx, vy = v.strip(" v=").split(',')
            velocities.append((int(vx), int(vy)))
    return positions, velocities


p, v = read_input("input")
print(p, v)

x_len = 101
y_len = 103
cur_p = p
for i in range(100):
    for i, (x, y) in enumerate(cur_p):
        dx, dy = v[i]
        nx = (x + dx) % x_len
        ny = (y + dy) % y_len
        cur_p[i] = (nx, ny)

x_mid = int((x_len-1)/2)
y_mid = int((y_len-1)/2)
quadrants = [((0, 0), (x_mid, y_mid)), ((0, y_mid+1), (x_mid, y_len)), (
    (x_mid+1, 0), (x_len, y_mid)), ((x_mid+1, y_mid+1), (x_len, y_len))]

sf = 1
for (min_x, min_y), (max_x, max_y) in quadrants:
    count = 0
    for x, y in cur_p:
        if min_x <= x < max_x and min_y <= y < max_y:
            count += 1
    sf *= count

print(sf)
