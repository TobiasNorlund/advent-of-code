import numpy as np
import heapq as hq 
from collections import namedtuple, defaultdict
from math import inf


h, w = 71, 71 #7, 7 # 
goal = (h-1, w-1)

with open("input.txt") as f:
    tiles = []
    for y, line in enumerate(f):
        x, y = line.strip().split(",")
        tiles.append((int(y), int(x)))

def build_map(tiles):
    m = np.zeros((h, w), dtype=bool)
    for y, x in tiles:
        m[int(y), int(x)] = True
    return m

def find_min_distance(m, start=(0, 0), goal=(h-1, w-1)):
    dist = defaultdict(lambda: inf)
    prev = {start: None}

    q = [(0, start[0], start[1])]
    hq.heapify(q)

    while len(q) > 0:

        num_steps, y, x = hq.heappop(q)
        next_states = []
        for y_next, x_next in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
            if 0<=y_next<h and 0<=x_next<w and not m[y_next, x_next]:
                next_states.append((num_steps+1, y_next, x_next))
        
        for next_steps, y_next, x_next in next_states:
            if next_steps < dist[(y_next, x_next)]:
                prev[(y_next, x_next)] = (x, y)
                dist[(y_next, x_next)] = next_steps
                hq.heappush(q, (next_steps, y_next, x_next))


    return dist[goal]

for n_tiles in range(1024, len(tiles)):
    m = build_map(tiles[:n_tiles+1])
    #print(tiles[n_tiles])
    #print(m)
    min_dist = find_min_distance(m)
    #print(n_tiles, min_dist)
    #print()
    if min_dist == inf:
        print(tiles[n_tiles][::-1])
        break