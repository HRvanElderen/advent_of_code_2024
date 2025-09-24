import statistics
X_LEN = 103
Y_LEN = 101


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


def display(points):
    for i in range(X_LEN):
        for j in range(Y_LEN):
            if (j, i) in points:
                print('#', end='')
            else:
                print('.', end="")
        print("")


def calc_sf(cur_p):
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    x_mid = X_LEN // 2
    y_mid = Y_LEN // 2
    for x, y in cur_p:
        if x < x_mid and y < y_mid:
            q1 += 1
        elif x > x_mid and y < y_mid:
            q2 += 1
        elif x < x_mid and y > y_mid:
            q3 += 1
        elif x > x_mid and y > y_mid:
            q4 += 1
    max(q1, q2, q3, q4)
    return q1 * q2 * q3 * q4


p, v = read_input("input")

min_sf = 9999999999
min_steps = 0
min_man_sum = 99999
for z in range(7414):
    x_vals = []
    y_vals = []
    for i, (x, y) in enumerate(p):
        dx, dy = v[i]
        nx = (x + dx) % X_LEN
        ny = (y + dy) % Y_LEN
        p[i] = (nx, ny)
        x_vals.append(nx)
        y_vals.append(ny)
    man_sum = 0
    for i in range(1, len(x_vals)):
        man_sum += abs(x_vals[0] - x_vals[i]) + abs(y_vals[0] - y_vals[i])
    # sf = calc_sf(p)
    stdev = statistics.stdev(x_vals) + statistics.stdev(y_vals)

    if man_sum < min_man_sum:
        min_man_sum = man_sum
        min_steps = z
display(p)


print(min_man_sum)
print(min_steps)
