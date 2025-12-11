def part1(t):
    def explore(key, guide):
        c = 0
        for option in guide[key]:
            if option == "out":
                return 1
            c += explore(option, guide)
        return c
    
    guide = {}
    
    for line in t.split("\n"):
        g = line.split()
        guide[g[0][:-1]] = g[1:]
    
    return explore("you", guide)


def part2(t):
    def explore(key, guide, dac, fft, mem):
        state = key, dac, fft
        if state in mem:
            return mem[state]
            
        c = 0
        for option in guide[key]:
            ndac = dac
            nfft = fft
            
            match option:
                case "dac": ndac = True
                case "fft": nfft = True
                
            if option == "out":
                mem[state] = 1 if ndac and nfft else 0
                return mem[state]
                
            c += explore(option, guide, ndac, nfft, mem)
            
        mem[state] = c
        return c
    
    guide = {}
    
    for line in t.split("\n"):
        g = line.split()
        guide[g[0][:-1]] = g[1:]
    
    return explore("svr", guide, False, False, {})


case1 = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

case2 = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""

print("part 1: %s\npart 2: %s" % (part1(case1), part2(case2)))
