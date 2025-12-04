lines = []
with open("input.txt") as f:
  for line in f:
    lines.append([int(c) for c in line.strip()])


def max_subseq(rem, seq):
    if len(seq) == 12:
        return int("".join(str(c) for c in seq))
    
    n = max(rem[:-(12-len(seq)-1) or None])
    i = rem.index(n)
    return max_subseq(rem[i+1:], seq + [n])

s=0
for line in lines:
  m = max_subseq(line, [])
  print(m)
  s+=m
print(s)
