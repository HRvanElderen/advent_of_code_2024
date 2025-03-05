import re

input = "input.txt"

lines = ""
with open(input, "r") as f:
    for line in f.readlines():
        lines += line
        
matches = re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)", lines)


total = 0
do = True
for match in matches:
    if match == "do()":
        do = True
    elif match == "don't()":
        do = False
    elif do:
        factors = re.findall("[0-9]+", match)
        total += int(factors[0]) * int(factors[1])

print(total)