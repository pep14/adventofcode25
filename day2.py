def part1():
    with open("input2.txt", "r") as f:
        data = f.read().split(",")

    rangeify = lambda x: range(int(x[0]), int(x[1]) + 1)
    formatted = [rangeify(i.split("-")) for i in data]
    
    nums = []
    for rng in formatted:
        for n in rng:
            s = str(n)
            l = len(s)

            mod = l % 2
            if mod: continue

            mid = l // 2
            if s[:mid] == s[mid:]: nums.append(n)

    return sum(nums)

def part2():
    with open("input2.txt", "r") as factors:
        data = factors.read().split(",")

    substringify = lambda s, l, f: [s[i : i + f] for i in range(0, l, f)]
    factorify = lambda x: [i for i in range(1, x) if x % i == 0]
    rangeify = lambda x: range(int(x[0]), int(x[1]) + 1)
    formatted = [rangeify(i.split("-")) for i in data]

    nums = []
    for rng in formatted:
        for n in rng:
            s = str(n)
            l = len(s)
            factors = factorify(l)

            for factor in factors:
                substrings = substringify(s, l, factor)
                if len(set(substrings)) == 1:
                    nums.append(n)
                    break

    return sum(nums)


print("part 1: %i\npart 2: %i" % (part1(), part2()))