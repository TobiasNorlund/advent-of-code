
res = []
with open("input.txt") as f:
    for line in f:
        a, b = line.strip().split(": ")
        res.append((int(a), [int(v) for v in b.split()]))


def rec(s, acc, rem):
    if len(rem) == 0:
        return s == acc
    elif acc > s:
        return False
    else:
        return rec(s, acc + rem[0], rem[1:]) or rec(s, acc * rem[0], rem[1:])

tot = 0
for sum, nums in res:
    if rec(sum, 0, nums):
        tot += sum

print(tot)