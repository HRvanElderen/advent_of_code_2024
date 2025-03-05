input = "input.txt"

reports = []
with open(input, "r") as f:
    for line in f.readlines():
        line = line.split()
        line = list(map(int, line))
        reports.append(line)


def check_order(list):
    if sorted(list) == list:
        return True
    elif sorted(list, reverse=True) == list:
        return True
    else:
        return False


def check_stepsize(list, min, max):
    for i in range(1, len(list)):
        stepsize = abs(list[i] - list[i - 1])
        if stepsize < min or stepsize > max:
            return False
    return True


def part_one():
    safe_count = 0
    for report in reports:
        if check_order(report):
            if check_stepsize(report, 1, 3):
                safe_count += 1
                print("safe")
            else:
                print("unsafe")
        else:
            print("unsafe")
    print("safe count: " + str(safe_count))


def check_report(report):
    if check_order(report):
        if check_stepsize(report, 1, 3):
            return True
        else:
            return False
    return False


def part_two():
    safe_count = 0
    for report in reports:
        if check_report(report):
            safe_count += 1
        else:
            # check list with one value less
            for i in range(0, len(report)):
                updated_list = [v for j, v in enumerate(report) if j != i]
                if check_report(updated_list):
                    safe_count += 1
                    break
    print("safe count: " + str(safe_count))


# part_one()
part_two()
