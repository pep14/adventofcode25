def part1():
    with open("input7.txt", "r") as f:
        t = f.read().split("\n")

    modpos = lambda p, dx, dy: [p[0] + dx, p[1] + dy]

    splitters = []
    start = [0, 0]
    total = 0

    for y, l in enumerate(t):
        for x, c in enumerate(l):
            pos = [x, y]

            match c:
                case "S":
                    start = pos
                case "^":
                    splitters.append(pos)
    
    beams = [modpos(start, 0, 1)]

    for step in range(len(t) - 2):
        beams_new = []

        for beam in beams:
            temp_beam = modpos(beam, 0, 1)

            if temp_beam in splitters:
                total += 1

                l, r = modpos(temp_beam, -1, 0), modpos(temp_beam,  1, 0)
                if l not in beams_new: beams_new.append(l)
                if r not in beams_new: beams_new.append(r)
            elif temp_beam not in beams_new:
                beams_new.append(temp_beam)
        
        beams = beams_new

    return total


def part2():
    with open("input7.txt", "r") as f:
        t = f.read().split("\n")

    modpos = lambda p, dx, dy: [p[0] + dx, p[1] + dy]

    splitters = []
    start = [0, 0]

    for y, l in enumerate(t):
        for x, c in enumerate(l):
            pos = [x, y]
            match c:
                case "S":
                    start = modpos(pos, 0, 1)
                case "^":
                    splitters.append(pos)

    beams = [[start[0], start[1], 1]]

    for step in range(len(t) - 2):
        beams_new = []

        for x, y, multiplicity in beams:
            temp_beam = modpos([x, y], 0, 1)

            if temp_beam in splitters:
                l, r = modpos(temp_beam, -1, 0), modpos(temp_beam,  1, 0)
                beams_new.append([l[0], l[1], multiplicity])
                beams_new.append([r[0], r[1], multiplicity])
            else:
                beams_new.append([temp_beam[0], temp_beam[1], multiplicity])

        beams_merged = []
        for beam_new in beams_new:
            for beam in beams_merged:
                if beam[0] == beam_new[0] and beam[1] == beam_new[1]:
                    beam[2] += beam_new[2]
                    break
            else:
                beams_merged.append(beam_new)

        beams = beams_merged

    return sum(beam[2] for beam in beams)


print("part 1: %i\npart 2: %i" % (part1(), part2()))
