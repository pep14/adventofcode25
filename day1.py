def part1():
    with open("input1.txt", "r") as f:
        data = f.read().split("\n")

    password = 0
    value = 50

    for l in data:
        R = (l[0] == "R")
        n = int(l[1:])

        value += n if R else -n
        value %= 100

        password += 1 if not value else 0

    return password


def part2():
    with open("input1.txt", "r") as f:
        data = f.read().split("\n")

    password = 0
    value = 50

    for l in data:
        R = (l[0] == "R")
        n = int(l[1:])

        a = (100 - value) % 100 if R \
            else value % 100

        if not a: a = 100

        if a <= n:
            password += 1 + (n - a) // 100

        value += n if R else -n

    return password

print("part 1: %i\npart 2: %i" % (part1(), part2()))