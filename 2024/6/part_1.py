
map = []

with open("input.txt") as f:
    for y, line in enumerate(f):
        map.append(line.strip())
        if "^" in line:
            start_pos = (y, line.index("^"))

w, h = len(map[0]), len(map)


visited_pos = [start_pos]
visited_map = [
    [[] for x in range(w)]
    for y in range(h)
]

turn = {
    "up": "right",
    "right": "down",
    "down": "left",
    "left": "up"
}

def valid(y, x):
    return 0 <= y < h and 0 <= x < w

def obstructed(y, x):
    return map[y][x] == "#"

def walk():

    dir = "up"

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
            break
            
        if obstructed(next_y, next_x):
            # turn
            dir = turn[dir]
            continue

        visited_pos.append((next_y, next_x))
        #print(visited_pos[-1])

    unique_visited_pos = set(visited_pos)
    #print(len(unique_visited_pos))

    return visited_map


if __name__ == "__main__":
    walk()