import numpy as np
from itertools import product


def read_maps():
    maps = []
    current_map = []
    for line in open("input.txt"):
        if line.strip() != "":
            current_map.append([c == "#" for c in line.strip()])
        else:
            maps.append(current_map)
            current_map = []
    maps.append(current_map)
    current_map = []  
    maps = [np.array(map) for map in maps]
    return maps


def part_1():
    maps = read_maps()

    tot = 0
    for map in maps:
        for c in range(1, map.shape[1]):
            if all(np.all(map[:, c-j] == map[:, c+j-1]) for j in range(1, min(c, map.shape[1]-c)+1)):
                # c is a valid column split point
                tot += c
                break

        for r in range(1, map.shape[0]):
            if all(np.all(map[r-j, :] == map[r+j-1, :]) for j in range(1, min(r, map.shape[0]-r)+1)):
                # r is a valid column split point
                tot += 100*r
                break

    print(tot)


def part_2():
    maps = read_maps()

    tot = 0
    for map in maps:

        # Try flipping all positions
        for x, y in product(range(map.shape[1]), range(map.shape[0])):

            map2 = map.copy()
            map2[y, x] = not map2[y, x]

            c_pos = None
            r_pos = None
            for c in range(1, map2.shape[1]):
                if all(np.all(map2[:, c-j] == map2[:, c+j-1]) for j in range(1, min(c, map2.shape[1]-c)+1)) and \
                    not all(np.all(map[:, c-j] == map[:, c+j-1]) for j in range(1, min(c, map.shape[1]-c)+1)):
                    # c is a valid _new_ column split point
                    c_pos = c
                    break
            else:
                for r in range(1, map2.shape[0]):
                    if all(np.all(map2[r-j, :] == map2[r+j-1, :]) for j in range(1, min(r, map2.shape[0]-r)+1)) and \
                        not all(np.all(map[r-j, :] == map[r+j-1, :]) for j in range(1, min(r, map.shape[0]-r)+1)):
                        # r is a valid _new_ column split point
                        r_pos = r
                        break

            if c_pos is not None:
                tot += c_pos
                break
            elif r_pos is not None:
                tot += 100*r_pos
                break

    print(tot)


if __name__ == "__main__":
    part_2()