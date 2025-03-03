from functools import lru_cache
from functools import cache
import time


test = "linen_test.txt"
input = "linen_input.txt"

with open(input, "r") as f:
    towels = f.readline().rstrip("\n")
    f.readline()  # seperator line
    patterns = []
    for line in f.read().splitlines():
        patterns.append(line)

towels = towels.split(sep=", ")
towels.sort(reverse=True)


@cache
def find_combination(target_pattern, current_pattern):
    if target_pattern == current_pattern:
        return True
    if current_pattern in target_pattern:
        for towel in towels:
            if towel not in target_pattern:
                continue
            result = find_combination(target_pattern, current_pattern + towel)
            if result:
                return True
    return False


def write_to_file(possible_patterns):
    with open("patterns.txt", "a") as f:
        f.write("\n".join(possible_patterns))


def solve():
    possible = 0
    possible_patterns = []
    start = time.time()
    for pattern in patterns:
        if find_combination(pattern, ""):
            possible_patterns.append(pattern)
            possible += 1
    end = time.time()
    print(end - start)
    # write_to_file(possible_patterns)
    return possible


# read all strings that are possible from file
def read_possible(file):
    with open(file, "r") as f:
        patterns = []
        for line in f.read().splitlines():
            patterns.append(line)
    return patterns


@cache
def find_all_combinations(target_pattern, current_pattern):
    if target_pattern == current_pattern:
        return 1
    result = 0
    if current_pattern in target_pattern:
        for towel in towels:
            if towel not in target_pattern:
                continue
            result += find_all_combinations(target_pattern, current_pattern + towel)
    return result


def solve_all():
    total_count = 0
    start = time.time()
    patterns = read_possible("patterns.txt")
    for pattern in patterns:
        total_count += find_all_combinations(pattern, "")
        print
    end = time.time()
    print(end - start)
    return total_count


print(solve_all())
