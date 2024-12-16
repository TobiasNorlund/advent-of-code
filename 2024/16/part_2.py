from queue import Queue, LifoQueue
from collections import namedtuple, defaultdict
import heapq as hq 
from math import inf

m = []

with open("input.txt") as f:
    for y, line in enumerate(f):
        m.append([c if c in ("#", ".", "S") else "." for c in line.strip()])
        if "S" in line:
            start_x = line.index("S")
            start_y = y
        if "E" in line:
            end_x = line.index("E")
            end_y = y

    h = y
    w = len(m[0])


State = namedtuple("State", ["score", "x", "y", "dir"])

prev = defaultdict(list)
dist = defaultdict(lambda: inf)
dist[(start_x, start_y, "R")] = 0

q = [State(0, start_x, start_y, "R")]
hq.heapify(q)


def step_forward(x, y, dir):
    if dir == "U":
        return x, y-1
    elif dir == "D":
        return x, y+1
    elif dir == "R":
        return x+1, y
    elif dir == "L":
        return x-1, y
    

turn_cw = {
    "U": "R",
    "R": "D",
    "D": "L",
    "L": "U"
}

turn_ccw = {
    "U": "L",
    "R": "U",
    "D": "R",
    "L": "D"
}


while len(q) > 0:

    score, x, y, dir = hq.heappop(q)

    next_states = []

    # step forward
    forw_x, forw_y = step_forward(x, y, dir)
    if 0 <= forw_x < w and 0 <= forw_y < h and m[forw_y][forw_x] == ".":
        next_states.append(State(score+1, forw_x, forw_y, dir))
    
    # turn CW
    next_states.append(State(score+1000, x, y, turn_cw[dir]))

    # turn CCW
    next_states.append(State(score+1000, x, y, turn_ccw[dir]))

    for next_state in next_states:
        ns = (next_state.x, next_state.y, next_state.dir)
        if next_state.score < dist[ns]:
            prev[ns] = [(x, y, dir)]
            dist[ns] = next_state.score
            hq.heappush(q, next_state)
        elif next_state.score == dist[ns] and (x, y, dir) not in prev[ns]:
            prev[ns].append((x, y, dir))
            hq.heappush(q, next_state)

min_score = min(
    dist[(end_x, end_y, "U")],
    dist[(end_x, end_y, "R")],
    dist[(end_x, end_y, "L")],
    dist[(end_x, end_y, "D")],
)

# find paths
steps = []
q = Queue()
for dir in ("U", "L", "R", "D"):
    if dist[(end_x, end_y, dir)] == min_score:
        q.put((end_x, end_y, dir))
while not q.empty():
    state = q.get()
    steps.insert(0, state)

    for p in prev[state]:
        q.put(p)

s = set((x, y) for x, y, _ in steps)

print(len(s))
