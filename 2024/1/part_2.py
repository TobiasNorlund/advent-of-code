from collections import Counter

file = "input.txt"

lst_1 = []
lst_2 = []

with open(file) as f:
    for line in f:
        d1, d2 = line.split()
        lst_1.append(int(d1))
        lst_2.append(int(d2))

counts = Counter(lst_2)

s = 0
for d in lst_1:
    s += d * counts[d]

print(s)