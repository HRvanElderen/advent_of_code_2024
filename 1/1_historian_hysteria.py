import numpy as np
input = "input.txt"

left = []
right  = []
with open(input, "r") as f:
    for line in f.readlines():
        line = line.split()

        left.append(int(line[0]))
        right.append(int(line[1]))

def calculate_sorted_difference(left, right):
    left.sort()
    right.sort()
    return sum(abs(np.subtract(left, right)))

def similarity_score(left, right):
    score = 0
    for number in left:
        score += number * right.count(number)
    return score

result = calculate_sorted_difference(left, right)
print("sorted difference: " + str(result))

result = similarity_score(left, right)
print("similarity score: " + str(result))