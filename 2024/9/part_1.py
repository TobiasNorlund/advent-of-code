

with open("input.txt") as f:
    inp = f.read().strip()

print(inp)

long = []

# Convert to long format
for i, c in enumerate(inp):
    if i % 2 == 0:
        # id
        long += [str(i // 2)] * int(c)
    else:
        # free space
        long += ["."] * int(c)

#print(long)

# Compact

first_free = 0
last = len(long) -1

while first_free < last:
    if long[first_free] != ".":
        first_free += 1
        continue
    if long[last] == ".":
        last -= 1
        continue

    long[first_free] = long[last]
    long[last] = "."

    #print(long)

# checksum
s = 0
for i, c in enumerate(long):
    if c == ".":
        break
    s += i * int(c)

print(s)