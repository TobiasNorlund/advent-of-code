import numpy as np
import heapq as hq 
from collections import namedtuple, defaultdict
from math import inf


h, w = 71, 71 #7, 7
m = np.zeros((h, w), dtype=bool)

goal = (h-1, w-1)

with open("input.txt") as f:
    for y, line in enumerate(f):
        if y >= 1024:
            break

        x, y = line.strip().split(",")
        m[int(y), int(x)] = True



dist = defaultdict(lambda: inf)
prev = {(0, 0): None}

q = [(0, 0, 0)]
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



print(dist[h-1, w-1])