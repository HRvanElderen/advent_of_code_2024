
def read_input(input):
    data = []
    with open(input, "r") as f:
        for line in f.readlines():
            n = []
            s, nums = line.split(sep=':')
            for i in nums.split():
                n.append(int(i))
            eq = (int(s), n)
            data.append(eq)
    return data


def rec(t, s, nums):
    if nums == []:
        return t == s
    else:
        next_num = nums[0]
        return rec(t, s * next_num, nums[1:]) or rec(t, s + next_num, nums[1:])


data = read_input("input.txt")

ops = ['*', '+']
total = 0
for t, nums in data:
    if rec(t, nums[0], nums[1:]):
        total += t

print(total)
