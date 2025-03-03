from functools import cache
import collections


def split_stone(stone):
    half = int(len(str(stone)) / 2)
    return int(str(stone)[:half]), int(str(stone)[half:])


def update_state(stone, d):
    if d in val_cache and stone in val_cache[d]:
        return val_cache[d][stone]
    if d == 0:
        result = 1
    elif stone == 0:
        result = update_state(1, d - 1)
    elif len(str(stone)) % 2 == 0:  # even
        left, right = split_stone(stone)
        result = update_state(left, d - 1) + update_state(right, d - 1)
    else:  # odd
        result = update_state(2024 * stone, d - 1)

    val_cache[d][stone] = result
    return result


def pretty_print(state):
    for i in state:
        print(i, end=" ")
    print("")


start_state = [8793800, 1629, 65, 5, 960, 0, 138983, 85629]
test_state = [125, 17]
state = start_state
iterations = 75

# print("initial state:")
# pretty_print(state)

# for i in range(0, iterations):
#     state = blink(state)
#     print("after iters:" + str(i + 1))
#     # pretty_print(state)
#     print(len(state))
total = 0
val_cache = collections.defaultdict(dict)
for i, v in enumerate(state):
    print(i)
    total += update_state(v, iterations)
    print("done")
print("total:" + str(total))
