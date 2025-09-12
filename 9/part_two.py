
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
            data_blocks.append(None)
        file = True

indices = [i for i, x in enumerate(data_blocks) if x == -1]
i = 0

blocks = []
free_spaces = []
size = 1
index = 0
prev = data_blocks[0]
start = 0
for data in data_blocks[1:]:
    if prev == data:
        size += 1
    else:
        if prev is None:
            free_spaces.append((start, size))
        else:
            blocks.append((start, index, size, prev))
            index += 1
        prev = data
        start += size
        size = 1
if prev == -1:
    free_spaces.append((start, size))
else:
    blocks.append((start, index, size, prev))
    index += 1

for start, index, size, data in reversed(blocks):
    for i, (free_start, free_size) in enumerate(free_spaces):
        if size <= free_size and start > free_start:
            blocks[index] = (free_start, index, size, data)
            free_spaces[i] = (free_start+size, free_size-size)
            break


block_arr = [None for i in range(len(data_blocks))]

for start, index, size, data in blocks:
    for i in range(start, start+size):
        block_arr[i] = data

checksum = 0
i = -1
for v in block_arr:
    i += 1
    if v is None:
        continue
    checksum += i*v


print(checksum)
