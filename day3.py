def general(total_digits):
    with open("input3.txt", "r") as f:
        data = [[int(j) for j in i] for i in f.read().split("\n")]

    total_joltage = 0

    for bank in data:
        local_joltage = ""

        digitremainder = total_digits - 1
        maxindex = size = len(bank)
        minindex = -1

        while digitremainder > 0:
            maxindex = bank[minindex + 1:].index(max(bank[minindex + 1:-digitremainder])) + minindex + 1
            minindex = maxindex
            digitremainder -= 1
            local_joltage += str(bank[maxindex])
        
        local_joltage += str(max(bank[minindex + 1:]))
        total_joltage += int(local_joltage)

    
    return total_joltage


print("part 1: %i\npart 2: %i" % (general(2), general(12)))