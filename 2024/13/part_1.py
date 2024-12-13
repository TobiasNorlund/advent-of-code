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
    A = np.array([[m.ax, m.bx], [m.ay, m.by]])
    b = np.array([m.price_x, m.price_y])
    
    try:
        res = np.linalg.solve(A, b)
        print(res)
        if np.isclose(res[0], round(res[0]), 1e-05) and np.isclose(res[1], round(res[1]), 1e-05) :
            tokens = res[0]*3 + res[1] * 1
            print(tokens)
            s += tokens
    except:
        pass

print(s)