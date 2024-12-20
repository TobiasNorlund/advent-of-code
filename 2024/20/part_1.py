import heapq as hq 
from collections import defaultdict, Counter
from math import inf
from copy import deepcopy

m = []
with open("input.txt") as f:
    for y, line in enumerate(f):
        m.append([c for c in line.strip()])
        if "S" in line:
            start = y, line.index("S")
        if "E" in line:
            end = y, line.index("E")

h, w = len(m), len(m[0])


def find_min_distance(m, start, goal):
    dist = defaultdict(lambda: inf)
    prev = {start: None}

    q = [(0, start[0], start[1])]
    hq.heapify(q)

    while len(q) > 0:

        num_steps, y, x = hq.heappop(q)
        next_states = []
        for y_next, x_next in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
            if 0<=y_next<h and 0<=x_next<w and m[y_next][x_next] in (".", "E"):
                next_states.append((num_steps+1, y_next, x_next))
        
        for next_steps, y_next, x_next in next_states:
            if next_steps < dist[(y_next, x_next)]:
                prev[(y_next, x_next)] = (x, y)
                dist[(y_next, x_next)] = next_steps
                hq.heappush(q, (next_steps, y_next, x_next))

    return dist[goal]

min_dist = find_min_distance(m, start, end)
c = Counter()

for y in range(1, h-1):
    for x in range(1, w-1):
        if m[y][x] == "#":
            # remove block
            new_map = deepcopy(m)
            new_map[y][x] = "."

            dist = find_min_distance(new_map, start, end)
            if dist < min_dist:
                print(y, x, min_dist-dist)
                c[min_dist-dist] += 1

s = 0
for save, count in c.items():
    if save >= 100:
        s += count

print(s)
