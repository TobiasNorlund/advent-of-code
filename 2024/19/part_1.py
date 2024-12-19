
with open("input.txt") as f:
    all_towels = f.readline().strip().split(", ")
    f.readline()
    patterns = [line.strip() for line in f]


def search(pattern: str, towels: list):
    if len(pattern) == 0:
        return []
    
    for towel in all_towels:
        if pattern.startswith(towel):
            rem = search(pattern[len(towel):], towels + [towel])
            if rem is not None:
                return towels + rem
            else:
                continue
    return None

s = 0
for pattern in patterns:
    m = search(pattern, [])
    if m is not None:
        print(pattern)
        s+=1

print(s)