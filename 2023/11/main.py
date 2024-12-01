import numpy as np
from itertools import combinations


def part_1():
    file = "input.txt"

    width = len(open(file).readline().strip())
    height = len(open(file).readlines())
    arr = np.zeros((height, width), dtype=bool)
    galaxies = []
    for y, row in enumerate(open(file)):
        for x, char in enumerate(row.strip()):
            if char == "#":
                arr[y, x] = True
                galaxies.append((x, y))
    
    empty_cols = []
    empty_rows = []
    for row in range(height):
        if arr[row, :].sum() == 0:
            empty_rows.append(row)
    for col in range(width):
        if arr[:, col].sum() == 0:
            empty_cols.append(col)

    #print(empty_rows)
    #print(empty_cols)

    #rows = list(range(height))
    #cols = list(range(width))

    #for r in empty_rows:
    #    rows.insert(r, None)
    #for c in empty_cols:
    #    cols.insert(c, None)
    
    rows_map = {r: r + (1000000-1)*sum(1 for x in empty_rows if x < r) for r in range(height)}
    cols_map = {c: c + (1000000-1)*sum(1 for x in empty_cols if x < c) for c in range(width)}

    tot = 0
    for (x1, y1), (x2, y2) in combinations(galaxies, r=2):
        tot += abs(cols_map[x1]-cols_map[x2]) + abs(rows_map[y1]-rows_map[y2])

    print(tot)

if __name__ == "__main__":
    part_1()