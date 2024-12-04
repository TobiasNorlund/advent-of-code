
inp = []

with open("input.txt") as f:
    for line in f:
        inp.append(line.strip())


w, h = len(inp[0]), len(inp)

s = 0

patterns = [
    [
        "M.S",
        ".A.",
        "M.S"
    ],[
        "M.M",
        ".A.",
        "S.S"
    ],[
        "S.M",
        ".A.",
        "S.M"
    ],[
        "S.S",
        ".A.",
        "M.M"
    ]
]

def pattern_match(p, inp, y, x):
    if (inp[y-1][x-1] == p[0][0]) and \
        (inp[y-1][x+1] == p[0][2]) and \
        (inp[y][x] == p[1][1]) and \
        (inp[y+1][x-1] == p[2][0]) and \
        (inp[y+1][x+1] == p[2][2]):
        return True

for y in range(1, h-1):
    for x in range(1, w-1):
        for p in patterns:
            if pattern_match(p, inp, y, x):
                s += 1

print(s)