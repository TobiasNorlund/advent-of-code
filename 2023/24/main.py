import numpy as np
from itertools import combinations
from collections import namedtuple
from sympy import symbols, solve, sqrt


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


HailStone = namedtuple("HailSton", ["x", "y", "z", "dx", "dy", "dz"])


def part_2():
    # each hailstone forms a line
    # I need to find a line that intersects with all those lines
    # To do that, it should be enough to take _any_ three lines, and find _the one_ intersecting line to that
    hail = []
    for line in open("input.txt"):
        pos, vel = line.strip().split("@")
        x, y, z = pos.split(", ")
        x, y, z = int(x), int(y), int(z)
        dx, dy, dz = vel.split(", ")
        dx, dy, dz = int(dx), int(dy), int(dz)
        hail.append(HailStone(x, y, z, dx, dy, dz))

    p1, p2, p3 = hail[0], hail[1], hail[2]

    t1 = symbols("t1")
    t2 = symbols("t2")
    t3 = symbols("t3")

    diff_1_x = p1.x + t1*p1.dx - p2.x - t2*p2.dx
    diff_2_x = p2.x + t2*p2.dx - p3.x - t3*p3.dx

    diff_1_y = p1.y + t1*p1.dy - p2.y - t2*p2.dy
    diff_2_y = p2.y + t2*p2.dy - p3.y - t3*p3.dy

    diff_1_z = p1.z + t1*p1.dz - p2.z - t2*p2.dz
    diff_2_z = p2.z + t2*p2.dz - p3.z - t3*p3.dz

    norm_diff_1 = sqrt(diff_1_x**2 + diff_1_y**2 + diff_1_z**2)
    norm_diff_2 = sqrt(diff_2_x**2 + diff_2_y**2 + diff_2_z**2)

    res = solve([
        diff_1_x / norm_diff_1 - diff_2_x / norm_diff_2,
        diff_1_y / norm_diff_1 - diff_2_y / norm_diff_2,
        diff_1_z / norm_diff_1 - diff_2_z / norm_diff_2,
    ], [t1, t2, t3], dict=True)

    print(res)


def part_2_2():
    hail = []
    for line in open("input.txt"):
        pos, vel = line.strip().split("@")
        x, y, z = pos.split(", ")
        x, y, z = int(x), int(y), int(z)
        dx, dy, dz = vel.split(", ")
        dx, dy, dz = int(dx), int(dy), int(dz)
        hail.append(HailStone(x, y, z, dx, dy, dz))

    p1, p2, p3 = hail[0], hail[1], hail[2]

    x0 = symbols("x0")
    y0 = symbols("y0")
    z0 = symbols("z0")
    vx = symbols("vx")
    vy = symbols("vy")
    vz = symbols("vz")

    res = solve([
        (x0 - p1.x)*(p1.dy - vy)-(y0 - p1.y)*(p1.dx - vx),
        (x0 - p1.x)*(p1.dz - vz)-(z0 - p1.z)*(p1.dx - vx),

        (x0 - p2.x)*(p2.dy - vy)-(y0 - p2.y)*(p2.dx - vx),
        (x0 - p2.x)*(p2.dz - vz)-(z0 - p2.z)*(p2.dx - vx),

        (x0 - p3.x)*(p3.dy - vy)-(y0 - p3.y)*(p3.dx - vx),
        (x0 - p3.x)*(p3.dz - vz)-(z0 - p3.z)*(p3.dx - vx),
    ])

    for r in res:
        print(r, r[x0]+r[y0]+r[z0])


if __name__ == "__main__":
    part_2_2()