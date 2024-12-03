
reports = []

with open("input.txt") as f:
    for line in f:
        reports.append([int(n) for n in line.split()])

num_safe = 0

def is_safe(r):
    return (all(n1 > n2 for n1, n2 in zip(r, r[1:])) or all(n2 > n1 for n1, n2 in zip(r, r[1:]))) and all(0 < abs(n1-n2) <  4 for n1, n2 in zip(r, r[1:]))


for r in reports:

    if is_safe(r):
        num_safe += 1
    else:
        for i in range(len(r)):
            if is_safe(r[:i] + r[i+1:]):
                num_safe += 1
                break


print(num_safe)