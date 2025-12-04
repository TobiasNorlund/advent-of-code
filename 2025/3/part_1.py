from itertools import combinations

lines = []
with open("input.txt") as f:
  for line in f:
    lines.append([int(c) for c in line.strip()])

s=0

for line in lines:
  m = max(int(str(a)+str(b)) for a,b in combinations(line, 2))
  print(m)
  s+=m
print(s)
