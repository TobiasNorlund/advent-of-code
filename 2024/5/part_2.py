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
failed = []
for i in range(len(pages)):
    print(pages[i])
    fail = False
    changed = True
    while changed:
        fail = False
        changed = False
        for p1, p2 in combinations(pages[i], 2):
            if fail:
                break
            for r1, r2 in rules:
                if p1 in (r1, r2) and p2 in (r1, r2):
                    if p1 == r1:
                        # Ok
                        pass
                    else:
                        print(p1, p2, "failed rule", r1, r2)
                        # Swap p1, p2 and restart
                        j1, j2 = pages[i].index(p1), pages[i].index(p2)
                        pages[i][j2] = p1
                        pages[i][j1] = p2
                        fail = True
                        if i not in failed:
                            failed.append(i)
                        changed = True
                        break
    print()


for page_i in failed:
    print(pages[page_i])
    print(f"adding {pages[page_i][len(pages[page_i])//2]}")
    s += pages[page_i][len(pages[page_i])//2]

print(s)