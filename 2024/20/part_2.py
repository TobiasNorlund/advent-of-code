import heapq as hq 
from collections import defaultdict
from itertools import combinations, product
from math import inf
from queue import Queue

m = []
with open("input.txt") as f:
    for y, line in enumerate(f):
        m.append([c for c in line.strip()])
        if "S" in line:
            start = y, line.index("S")
        if "E" in line:
            end = y, line.index("E")

h, w = len(m), len(m[0])


def find_distances_from_point(m, start):
    dist = defaultdict(lambda: inf)
    dist[start] = 0
    prev = {start: None}

    q = [(0, start[0], start[1])]
    hq.heapify(q)

    while len(q) > 0:

        num_steps, y, x = hq.heappop(q)
        next_states = []
        for y_next, x_next in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
            if 0<=y_next<h and 0<=x_next<w and m[y_next][x_next] in (".", "S"):
                next_states.append((num_steps+1, y_next, x_next))
        
        for next_steps, y_next, x_next in next_states:
            if next_steps < dist[(y_next, x_next)]:
                prev[(y_next, x_next)] = (x, y)
                dist[(y_next, x_next)] = next_steps
                hq.heappush(q, (next_steps, y_next, x_next))

    return dist

dist_to_end = find_distances_from_point(m, end)

walkable_pos = []
for cheat_start_y in range(1, h-1):
    for cheat_start_x in range(1, w-1):
        if m[cheat_start_y][cheat_start_x] in (".", "S", "E"):
            walkable_pos.append((cheat_start_y, cheat_start_x))


def hamming_dist(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])


counter = defaultdict(lambda: 0)
for cheat_start, cheat_end in product(walkable_pos, repeat=2):
    if (cheat_len := hamming_dist(cheat_start, cheat_end)) <= 20:
        save = dist_to_end[cheat_start] - dist_to_end[cheat_end] - cheat_len
        if save >= 100:
            counter[save] += 1


counts = [c for c in counter.items()]
counts = sorted(counts, key=lambda x: x[0])
s = 0
for save, count in counts:
    print(save, count)
    s += count

print(s)