import re
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

robs = [] 
with open("input.txt") as f:
    for line in f:
        robot = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line.strip()).groups()
        robot = [int(n) for n in robot]
        robs.append(robot)

w, h = 101, 103

for step in range(1, 10000):

    for i in range(len(robs)):
        x, y, vx, vy = robs[i]

        #print(robs[i])

        # update 
        robs[i][0] = (x + vx) % w
        robs[i][1] = (y + vy) % h

    if step > 7000 and (step in [270 + 103*i for i in range(100)] or step in [317 + 101*i for i in range(100)]):
        m = np.zeros((h, w), dtype=np.int32)

        for x, y, _, _ in robs:
            m[y, x] += 1

        plt.imshow(m)
        plt.title(f"After {step} seconds:")
        plt.show()  # Show the image without blocking execution