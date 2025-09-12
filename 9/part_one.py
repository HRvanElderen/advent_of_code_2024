
def read_input(input):
    with open(input, "r") as f:
        return f.readline()


data = read_input("input.txt")

file = True
file_id = 0
data_blocks = []
for i in data:
    if file:
        for i in range(int(i)):
            data_blocks.append(file_id)
        file_id += 1
        file = False
    else:
        for i in range(int(i)):
            data_blocks.append(-1)
        file = True

indices = [i for i, x in enumerate(data_blocks) if x == -1]
i = 0

while -1 in data_blocks:
    last = data_blocks[-1]
    if last != -1:
        data_blocks[indices[i]] = last
        i += 1
    data_blocks = data_blocks[:-1]

checksum = 0
for i, v in enumerate(data_blocks):
    checksum += i*v

print(checksum)
