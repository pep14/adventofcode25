import math


def part1():
    with open("input8.txt", "r") as f:
        points: list[str] = [[int(v) for v in line.split(",")] for line in f.read().split("\n")]
    
    v3dist = lambda a, b: sum((a[i] - b[i]) ** 2 for i in range(3))
    pairs = []
    circuits: list[list] = []
    
    for i, a in enumerate(points):
        for j, b in enumerate(points):
            if i >= j:
                continue
            d = v3dist(a, b)
            pairs.append([i, j, d])

    pairs.sort(key=lambda p: p[2])
    
    for p in pairs[:1000]:
        a = p[0]
        b = p[1]
        ca = None
        cb = None

        for c in circuits:
            if a in c:
                ca = c
            if b in c:
                cb = c

        if not ca and not cb: circuits.append([a, b])
        elif ca and not cb: ca.append(b)
        elif not ca and cb: cb.append(a)
        elif ca != cb:
            ca.extend(cb)
            circuits.remove(cb)
        
    used = [i for c in circuits for i in c]
    for i in range(len(points)):
        if i not in used:
            circuits.append([i])

    lengths = sorted([len(c) for c in circuits], reverse=True)
    return lengths[0] * lengths[1] * lengths[2]


def part2():
    with open("input8.txt", "r") as f:
        points: list[str] = [[int(v) for v in line.split(",")] for line in f.read().split("\n")]
    
    v3dist = lambda a, b: sum((a[i] - b[i]) ** 2 for i in range(3))
    pairs = []
    circuits: list[list] = [[i] for i in range(len(points))]
    
    for i, a in enumerate(points):
        for j, b in enumerate(points):
            if i >= j:
                continue
            d = v3dist(a, b)
            pairs.append([i, j, d])

    pairs.sort(key=lambda p: p[2])
    
    last_pair = None

    for p in pairs:
        a = p[0]
        b = p[1]
        ca = None
        cb = None

        for c in circuits:
            if a in c:
                ca = c
            if b in c:
                cb = c

        if not ca and not cb:
            circuits.append([a, b])
            last_pair = [a, b]
        elif ca and not cb:
            ca.append(b)
            last_pair = [a, b]
        elif not ca and cb:
            cb.append(a)
            last_pair = [a, b]
        elif ca != cb:
            ca.extend(cb)
            circuits.remove(cb)
            last_pair = [a, b]
        
        if len(circuits) == 1:
            break

    return points[last_pair[0]][0] * points[last_pair[1]][0]


print("part 1: %i\npart 2: %i" % (part1(), part2()))
