m = []
trailheads = []
with open("input.txt") as f:
    for y, line in enumerate(f):
        m.append([])
        for x, c in enumerate(line.strip()):
            m[y].append(int(c) if c != "." else -1)
            if c == "0":
                trailheads.append((y, x))

h, w = len(m), len(m[0])

print(trailheads)

def get_trails(y, x, prev):
    if not (0 <= y < h and 0 <= x < w and m[y][x] == prev+1):
        return set()
    
    n = m[y][x]

    if n == 9:
        return set([(y, x)])
    else:
        return get_trails(y-1, x, n) | \
            get_trails(y+1, x, n) | \
            get_trails(y, x-1, n) | \
            get_trails(y, x+1, n)
    
s = 0
for y, x in trailheads:
    ends = get_trails(y, x, -1)
    s += len(ends)

print(s)