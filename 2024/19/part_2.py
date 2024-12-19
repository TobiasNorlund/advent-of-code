from functools import cache

with open("input.txt") as f:
    all_towels = f.readline().strip().split(", ")
    f.readline()
    patterns = [line.strip() for line in f]


@cache
def search(pattern: str):
    if len(pattern) == 0:
        return 1
    
    n_matches = 0
    for towel in all_towels:
        if pattern.startswith(towel):
            n_matches += search(pattern[len(towel):])
    return n_matches

s = 0
for pattern in patterns:
    n_matches = search(pattern)
    print(pattern, n_matches)
    s += n_matches

print(s)
