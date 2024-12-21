from math import inf
from collections import defaultdict

codes = []
with open("input.txt") as f:
    for line in f:
        codes.append(line.strip())

# from A to B on directional, using directional
DIR_BUTTONS = ("A", "^", "<", ">", "v")
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
        "^": ["^<", "<^"],
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
NUM_BUTTONS = ("A", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
dir2num = {
    c1: {
        c2: dir2num_all_paths(c1, c2, "", c1)
        for c2 in NUM_BUTTONS
    }
    for c1 in NUM_BUTTONS
}

"""
Strategy:

dp[level][from][to] = min( sum( dp[level-1][f][t] for f, t in alt.bigrams) for alt in dir2dir[from][to])
"""

def bigrams(seq):
    return zip(seq[:-1], seq[1:])

# Add initial level
dp = [{}]
for f in DIR_BUTTONS:
    dp[0][f] = {
        t: len(dir2dir[f][t][0]) + 1
        for t in DIR_BUTTONS
    }

# Add other dir2dir levels
for level in range(1, 25):
    dp.append(defaultdict(dict))
    for from_ in DIR_BUTTONS:
        for to_ in DIR_BUTTONS:
            dp[level][from_][to_] = min(
                sum(
                    dp[level-1][f][t] for f, t in bigrams("A"+alt+"A")
                )
                for alt in dir2dir[from_][to_]
            )

# Add final num2dir layer
dp.append(defaultdict(dict))
level = len(dp)-1
for from_ in NUM_BUTTONS:
    for to_ in NUM_BUTTONS:
        dp[level][from_][to_] = min(
            sum(
                dp[level-1][f][t] for f, t in bigrams("A"+alt+"A")
            )
            for alt in dir2num[from_][to_]
        )

compl = 0
for code in codes:
    s = 0
    print(code+":")
    for f, t in bigrams("A"+code):
        #print(f, t, dp[-1][f][t])
        s += dp[-1][f][t]
    print(s, "*", int(code[:-1]))
    print()
    compl += s * int(code[:-1])

print(compl)