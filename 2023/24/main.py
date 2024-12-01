import re
from itertools import combinations


def get_intersection(x1, y1, dx1, dy1, x2, y2, dx2, dy2):
    k1 = dy1/dx1
    k2 = dy2/dx2

    m1 = y1-k1*x1
    m2 = y2-k2*x2

    #intersection point
    if k1 == k2:
        # parallell lines
        return None
    
    x = (m2-m1)/(k1-k2)
    y = k1*x + m1

    # time
    t1 = (x-x1)/dx1
    t2 = (x-x2)/dx2

    return x, y, t1, t2


def part_1():
    hail = []
    for line in open("input.txt"):
        pos, vel = line.strip().split("@")
        x, y, z = pos.split(", ")
        x, y, z = int(x), int(y), int(z)
        dx, dy, dz = vel.split(", ")
        dx, dy, dz = int(dx), int(dy), int(dz)
        hail.append((x, y, z, dx, dy, dz))

    tot = 0
    for ex1, ex2 in combinations(hail, 2):
        x1, y1, _, dx1, dy1, _ = ex1
        x2, y2, _, dx2, dy2, _ = ex2
        intersection = get_intersection(x1, y1, dx1, dy1, x2, y2, dx2, dy2)
        if intersection is None:
            #print(x1, y1, x2, y2, "parallell")
            continue

        x, y, t1, t2 = intersection
        #print(x1, y1, x2, y2, " ---> ", x, y, t1, t2)

        #min, max = 7, 27
        min, max = 200000000000000, 400000000000000
        if x is not None and min <= x <= max and min <= y <= max and t1 >= 0 and t2 >= 0:
            tot += 1
        
    print(tot)



if __name__ == "__main__":
    part_1()