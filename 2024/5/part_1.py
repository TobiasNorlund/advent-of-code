from itertools import combinations

rules = []
pages = []

r = True

with open("input.txt") as f:
    for line in f:
        if line == "\n":
            r = False
            continue
        if r:
            rules.append([int(n) for n in line.strip().split("|")])
        else:
            pages.append([int(n) for n in line.strip().split(",")])


s = 0
for page in pages:
    print(page)
    fail = False
    for p1, p2 in combinations(page, 2):
        if fail:
            break
        for r1, r2 in rules:
            if fail:
                break
            if p1 in (r1, r2) and p2 in (r1, r2):
                if p1 == r1:
                    # Ok
                    pass
                else:
                    print(p1, p2, "failed rule", r1, r2)
                    fail = True
                    break
    if not fail:
        print(f"adding {page[len(page)//2]}")
        s += page[len(page)//2]
    print()

print(s)