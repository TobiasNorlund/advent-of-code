


def part_1():
    histories = [[int(n) for n in line.split()] for line in open("input.txt")]
    
    def rec(hist):
        diffs = [n2 - n1 for n1, n2 in zip(hist[:-1], hist[1:])]
        if all(n == 0 for n in diffs):
            return hist[-1]
        else:
            return hist[-1] + rec(diffs)

    tot = 0
    for hist in histories:
        tot += rec(hist)
    
    print(tot)


def part_2():
    histories = [[int(n) for n in line.split()] for line in open("input.txt")]

    def rec(hist):
        diffs = [n2 - n1 for n1, n2 in zip(hist[:-1], hist[1:])]
        if all(n == 0 for n in diffs):
            return hist[0]
        else:
            return hist[0] - rec(diffs)
    
    tot = 0
    for hist in histories:
        tot += rec(hist)
    
    print(tot)


if __name__ == "__main__":
    part_2()