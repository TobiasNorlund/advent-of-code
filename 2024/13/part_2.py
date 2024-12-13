import re
from collections import namedtuple
import numpy as np

Machine = namedtuple("Machine", "ax ay bx by price_x price_y")

with open("input.txt") as f:
    machines = []
    n = "\n"
    while n == "\n":
        button_a = f.readline().strip()
        button_b = f.readline().strip()
        price = f.readline().strip()
        n = f.readline()

        a = re.match(r"Button A: X\+(\d+), Y\+(\d+)", button_a)
        b = re.match(r"Button B: X\+(\d+), Y\+(\d+)", button_b)
        p = re.match(r"Prize: X=(\d+), Y=(\d+)", price)

        m = Machine(ax=int(a.group(1)), ay=int(a.group(2)), bx=int(b.group(1)), by=int(b.group(2)), price_x=int(p.group(1)), price_y=int(p.group(2)))
        machines.append(m)

        print(m)


s = 0
for m in machines:
    a1 = m.ax
    b1 = m.bx
    c1 = m.price_x + 10000000000000

    a2 = m.ay
    b2 = m.by
    c2 = m.price_y + 10000000000000

    x = (c2*b1 - c1*b2) / (a2*b1-a1*b2)
    y = (c1*a2-c2*a1) / (a2*b1-a1*b2)

    if x.is_integer() and y.is_integer():
        tokens = int(x*3 + y*1)
        s += tokens

print(s)