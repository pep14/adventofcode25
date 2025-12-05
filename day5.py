def part1():
    with open("input5.txt", "r") as f:
        t = f.read().split("\n")
        
    ranges = []
    total = 0
    
    for line in t:
        if not line: continue
        temp = line.split("-")
        if temp[0] != line:
            ranges.append(range(
                int(temp[0]), int(temp[1]) + 1
            ))
            continue
        for r in ranges:
            if int(line) in r:
                total += 1
                break
    
    return total


def part2():
    with open("input5.txt", "r") as f:
        t = f.read().split("\n")
        
    ranges_overlapping = []
    ranges = []
    
    for line in t:
        if not line: continue
        temp = line.split("-")
        if temp[0] != line:
            ranges_overlapping.append([int(temp[0]), int(temp[1])])
            continue
    
    ranges_overlapping.sort(key=lambda x: x[0])
    print(ranges_overlapping)
    print(ranges)
    
    for r in ranges_overlapping:
        found = False
        for a in ranges:
            if a[0] <= r[0] <= a[1]:
                if r[1] > a[1]:
                    ranges[ranges.index(a)] = [a[0], r[1]]
                found = True
                break
        if not found:
            ranges.append(r)
    
    print(ranges)
    
    range_sizes = [
        r[1] - r[0] + 1
        for r in ranges
    ]
    
    return sum(range_sizes)


print("part 1: %i\npart 2: %i" % (part1(), part2()))
