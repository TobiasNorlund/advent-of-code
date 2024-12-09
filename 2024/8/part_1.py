from collections import defaultdict
from itertools import combinations
import numpy as np

map = []
locs = defaultdict(list)

with open("input.txt") as f:
    for y, line in enumerate(f):
        l = line.strip()
        map.append(l)
        for x, c in enumerate(l):
            if c != ".":
                locs[c].append((y, x))

    h = y+1
    w = len(l)

print(h, w)

antinodes = np.zeros((h, w))
for c, locations in locs.items():
    for (y1, x1), (y2, x2) in combinations(locations, 2):
        delta_y = y1 - y2
        delta_x = x1 - x2

        if 0 <= y2 - delta_y < h and 0 <= x2 - delta_x < w:
            antinodes[y2 - delta_y, x2 - delta_x] = 1
        if 0 <= y1 + delta_y < h and 0 <= x1 + delta_x < w:
            antinodes[y1 + delta_y, x1 + delta_x] = 1

print(antinodes)
print(antinodes.sum())