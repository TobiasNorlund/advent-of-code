from itertools import combinations, product

with open("input.txt") as f:
    key_or_lock = None
    is_lock = None
    keys = []
    locks = []
    for line in f:
        if line == "\n":
            if is_lock:
                locks.append(key_or_lock)
            else:
                keys.append(key_or_lock)
            is_lock = None
            continue
        if is_lock is None:
            #reset
            is_lock = all(c == "#" for c in line.strip())
            key_or_lock = [-1, -1, -1, -1, -1]
        for i, c in enumerate(line.strip()):
            key_or_lock[i] += 1 if c == "#" else 0
        
# print(keys)
# print(locks)

s = 0
for key, lock in product(keys, locks):
    if all(key[i]+lock[i] <= 5 for i in range(5)):
        s += 1

print(s)