import math

def part1():
    with open("input6.txt", "r") as f:
        t = f.read().split("\n")

    arr: list[list] = []
    total = 0

    for line in t:
        items = line.split()
        for i, v in enumerate(items):
            if i == len(arr):
                arr.append([])
            if v in ["*", "+"]:
                arr[i].append(v)
                continue
            arr[i].append(int(v))

    for i, local_arr in enumerate(arr):
        local_total = 0

        match local_arr[-1]:
            case "+":
                local_total += sum(local_arr[:-1])
            case "*":
                local_total += math.prod(local_arr[:-1])
        
        total += local_total


    return total

def part2():
    with open("input6.txt", "r") as f:
        t = f.read().split("\n")

    strings = []
    arr: list[list] = []
    total = 0

    for line in t:
        for i, char in enumerate(line):
            if i == len(strings):
                strings.append(char)
                continue

            strings[i] += char

    for string in strings:
        if not string.strip():
            continue

        operator = string[-1]
        if operator.strip():
            arr.append([operator])

        arr[-1].insert(0, int(string[:-1]))

    for i, local_arr in enumerate(arr):
        local_total = 0

        match local_arr[-1]:
            case "+":
                local_total += sum(local_arr[:-1])
            case "*":
                local_total += math.prod(local_arr[:-1])
        
        total += local_total


    return total

print("part 1: %i\npart 2: %i" % (part1(), part2()))
