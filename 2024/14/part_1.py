import re

robs = [] 
with open("input.txt") as f:
    for line in f:
        robot = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line.strip()).groups()
        robot = [int(n) for n in robot]
        robs.append(robot)

w, h = 101, 103

for step in range(100):

    for i in range(len(robs)):
        x, y, vx, vy = robs[i]

        #print(robs[i])

        # update 
        robs[i][0] = (x + vx) % w
        robs[i][1] = (y + vy) % h

        

print(robs)

quadrants = [[], [], [], []]
for r in robs:
    x, y, _, _ = r
    if x < (w // 2):
        if y < (h // 2):
            quadrants[0].append(r)
        elif y > (h // 2):
            quadrants[2].append(r)
    elif x > (w // 2):
        if y < (h // 2):
            quadrants[1].append(r)
        elif y > (h // 2):
            quadrants[3].append(r)

s = 1
for q in quadrants:
    s *= len(q)

print(s)

