from itertools import product
from math import inf


codes = []
with open("input.txt") as f:
    for line in f:
        codes.append(line.strip())

# from A to B on durectional, using directional
dir2dir = {
    "A": {
        "A": [""],
        "^": ["<"],
        ">": ["v"],
        "v": ["v<", "<v"],
        "<": ["v<<", "<v<"]
    },
    "^": {
        "A": [">"],
        "^": [""],
        ">": ["v>", ">v"],
        "v": ["v"],
        "<": ["v<"]
    },
    ">": {
        "A": ["^"],
        "^": ["^<", "^<"],
        ">": [""],
        "v": ["<"],
        "<": ["<<"]
    },
    "v": {
        "A": ["^>", ">^"],
        "^": ["^"],
        ">": [">"],
        "v": [""],
        "<": ["<"]
    },
    "<": {
        "A": [">>^", ">^>"],
        "^": [">^"],
        ">": [">>"],
        "v": [">"],
        "<": [""]
    }
}

dir2num_nn = {
    "A": [("0", "<"), ("3", "^")],
    "0": [("2", "^"), ("A", ">")],
    "1": [("4", "^"), ("2", ">")],
    "2": [("1", "<"), ("5", "^"), ("3", ">"), ("0", "v")],
    "3": [("6", "^"), ("2", "<"), ("A", "v")],
    "4": [("7", "^"), ("5", ">"), ("1", "v")],
    "5": [("8", "^"), ("4", "<"), ("2", "v"), ("6", ">")],
    "6": [("9", "^"), ("5", "<"), ("3", "v")],
    "7": [("8", ">"), ("4", "v")],
    "8": [("7", "<"), ("5", "v"), ("9", ">")],
    "9": [("8", "<"), ("6", "v")],
}

def dir2num_all_paths(cur, to, path, visited):
    if cur == to:
        return [path]
    
    paths = []
    for n, dir in dir2num_nn[cur]:
        if n not in visited:
            paths += dir2num_all_paths(n, to, path+dir, visited+n)

    if len(paths) == 0:
        return []
    else:
        min_path_len = min(len(p) for p in paths)
        return [p for p in paths if len(p) == min_path_len]

# from A to B on numeric, using directional
dir2num = {
    c1: {
        c2: dir2num_all_paths(c1, c2, "", c1)
        for c2 in "A0123456789"
    }
    for c1 in "A0123456789"
}

"""
Strategy:

BFS over full sequence
for each level, we get some alternative paths
if it's the lowest level, we return the shortest path amonth the alternatives

"""


robots = [dir2num, dir2dir, dir2dir]

def get_min_path(path, robots) -> int:
    map = robots[0]

    # expand path alternatives
    alts = []
    state = "A"  # Always start from A at each level
    for p in path:
        alts.append(map[state][p])
        state = p

    if len(robots) == 1:
        # just return the shortest path
        return sum(len(alt[0])+1 for alt in alts)
    else:
        # return the min of running get_min_path on all alternatives 
        min_path = inf
        for alt_path in product(*alts):
            if (m := get_min_path("A".join(alt_path)+"A", robots[1:])) < min_path:
                min_path = m
        return min_path
    
s = 0
for c in codes:
    s += get_min_path(c, robots) * int(c[:-1])

print(s)