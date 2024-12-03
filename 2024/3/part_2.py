import re

input = "input.txt"

with open(input) as f:
    text = f.read()

s = 0
c = True

for m in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", text):
    if m == "do()":
        c = True
    elif m == "don't()":
        c = False
    elif c == True:
        d1, d2 = re.match(r"mul\((\d+),(\d+)\)", m).groups()
        d1,  d2 = int(d1), int(d2)
        s += d1 * d2

print(s)