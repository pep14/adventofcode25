def part1():
    with open("input4.txt", "r") as f:
        t = f.read().split("\n")
    
    rolls = []

    for y, v in enumerate(t):
        for x, c in enumerate(v):
            if c == "@":
                rolls.append([x, y])

    total = 0

    
    for roll in rolls:
        adjacents = [
            [roll[0] - dx, roll[1] - dy]
             for dx in [-1, 0, 1]
             for dy in [-1, 0, 1]
             if not (dx == 0 and dy == 0)
        ]

        total_valid_adjacents = 0
        for adjacent in adjacents:
            if adjacent in rolls:
                total_valid_adjacents += 1

        if total_valid_adjacents < 4:
            total += 1

    return total


def part2():
    with open("input4.txt", "r") as f:
        t = f.read().split("\n")

    rolls = []
    rolls_old = []

    for y, v in enumerate(t):
        for x, c in enumerate(v):
            if c == "@":
                rolls.append([x, y])

    total = 0

    while rolls_old != rolls:
        rolls_old = rolls.copy()
        for roll in rolls:
            adjacents = [
                [roll[0] - dx, roll[1] - dy]
                 for dx in [-1, 0, 1]
                 for dy in [-1, 0, 1]
                 if not (dx == 0 and dy == 0)
            ]

            total_valid_adjacents = 0
            for adjacent in adjacents:
                if adjacent in rolls:
                    total_valid_adjacents += 1

            if total_valid_adjacents < 4:
                total += 1
                rolls.pop(rolls.index(roll))

    return total


print("part 1: %i\npart 2: %i" % (part1(), part2()))
