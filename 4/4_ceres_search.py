import numpy as np

input = "input.txt"

def read_input(input):
    data = []
    with open(input, "r") as f:
        for line in f.readlines():
            row = []
            for i in line.rstrip("\n"):
                row.append(i)
            data.append(row)
    return data


def horizontal(data, word):
    matches = 0
    for row in data:
        for i in range(len(row) - len(word) + 1):
            equal = True
            for j in range(len(word)):
                if row[i + j] != word[j]:
                    equal = False
                    break
            if equal:
                matches += 1
    return matches

def diagonal(data, word):
    diag_count = 2*len(data[0])-1
    diags = []
    for n in range(diag_count):
        diag = []
        for i, row in enumerate(data):
            for j, v in enumerate(row):
                if i+j == n:
                    diag.append(v)
        if len(diag) >= len(word): 
            diags.append(diag)

    return horizontal(diags, word) + horizontal(diags, list(reversed(word)))
    

def find_matches(data):
    total = 0
    word = ['X', 'M', 'A', 'S']
    rev_word = list(reversed(word))
    total += horizontal(data, word)
    total += horizontal(data, rev_word) 
    transpose_data = np.transpose(np.array(data))
    total += horizontal(transpose_data, word)
    total += horizontal(transpose_data, rev_word)
    total += diagonal(data, word)
    total += diagonal(np.flip(data,0), word)
    return total

def part_one():
    data = read_input(input)
    result = find_matches(data)
    print(result)

def part_two():
    data = read_input(input)
    count = 0
    for i, row in enumerate(data):
        for j, v in enumerate(row):
            if v == 'A' and j > 0 and j < len(row)-1 and i > 0 and i < len(data) - 1:
                if (data[i-1][j-1] == 'M' and data[i+1][j-1] == 'M' and data[i+1][j+1] == 'S' and data[i-1][j+1] == 'S') \
                or (data[i-1][j-1] == 'M' and data[i+1][j-1] == 'S' and data[i+1][j+1] == 'S' and data[i-1][j+1] == 'M') \
                or (data[i-1][j-1] == 'S' and data[i+1][j-1] == 'M' and data[i+1][j+1] == 'M' and data[i-1][j+1] == 'S') \
                or (data[i-1][j-1] == 'S' and data[i+1][j-1] == 'S' and data[i+1][j+1] == 'M' and data[i-1][j+1] == 'M'):
                    count += 1
    print(count)

part_two()