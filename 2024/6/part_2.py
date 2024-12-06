from copy import deepcopy
from part_1 import walk as part_1_walk

map = []

with open("input.txt") as f:
    for y, line in enumerate(f):
        map.append([c for c in line.strip()])
        if "^" in line:
            start_pos = (y, line.index("^"))

w, h = len(map[0]), len(map)

turn = {
    "up": "right",
    "right": "down",
    "down": "left",
    "left": "up"
}

def valid(y, x):
    return 0 <= y < h and 0 <= x < w

def obstructed(y, x, map):
    return map[y][x] == "#"

def walk(start_pos, start_dir, map):

    visited_pos = [start_pos]
    visited_map = [
        [[] for x in range(w)]
        for y in range(h)
    ]

    dir = start_dir

    while 0 <= (y := visited_pos[-1][0]) < h and 0 <= (x := visited_pos[-1][1]) < w:

        visited_map[y][x].append(dir)

        # step
        if dir == "up":
            next_y = y-1
            next_x = x
        elif dir == "right":
            next_y = y
            next_x = x+1
        elif dir == "down":
            next_y = y+1
            next_x = x
        elif dir == "left":
            next_y = y
            next_x = x-1

        if not valid(next_y, next_x):
            # We've stepped out
            return "stepped out"
            
        if obstructed(next_y, next_x, map):
            # turn
            dir = turn[dir]

            # If we've been here before
            if dir in visited_map[y][x]:
                # We've hit a loop
                return "loop"
            else:
                continue

        visited_pos.append((next_y, next_x))


visited_map = part_1_walk()

# For each position, check if putting a block here would create a loop
loop_pos = []
for y in range(h):
    for x in range(w):
        for ny, nx, cur_dir in [(y-1, x, "down"), (y, x+1, "left"), (y+1, x, "up"), (y, x-1, "right")]:
            if valid(ny, nx) and map[y][x] == ".":
                if cur_dir in visited_map[ny][nx]:
                    # Test if I'll come back if I start here and go turn[cur_dir]
                    print(f"test", ny, nx, turn[cur_dir])

                    test_map = deepcopy(map)
                    test_map[y][x] = "#"

                    if walk(start_pos=start_pos, start_dir="up", map=test_map) == "loop":
                        print("found loop at", ny, nx, turn[cur_dir])
                        loop_pos.append((y, x))
                        break


print(loop_pos)
print(len(loop_pos))