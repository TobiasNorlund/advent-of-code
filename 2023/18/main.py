import numpy as np



def print_map(map):
    for y in range(map.shape[0]):
        print("".join(["#" if map[y, x] else "." for x in range(map.shape[1])]))


def part_1():
    file = "input.txt"
    height = 10000 # len(open(file).readlines())
    width = 10000# len(open(file).readline().strip())

    map = np.zeros((height, width), dtype=bool)

    x = 5000
    y = 5000
    for line in open(file):
        direction, length, _ = line.split()
        length = int(length)
        if direction == "R":
            for x in range(x+1, x + length+1):
                map[y, x] = True
        elif direction == "L":
            for x in range(x-1, x - length-1, -1):
                map[y, x] = True
        elif direction == "U":
            for y in range(y-1, y - length-1, -1):
                map[y, x] = True
        elif direction == "D":
            for y in range(y+1, y + length+1):
                map[y, x] = True

    #print_map(map)
    #print()

    # fill
    q = [(5001, 5001)]
    while len(q) > 0:
        x, y = q.pop()

        for new_y in [y-1, y, y+1]:
            for new_x in [x-1, x, x+1]:
                if not (0 <= new_x < width) or not (0 <= new_y < height):
                    print(new_x, new_y)
                    raise RuntimeError()

                if not map[new_y, new_x] and (new_x, new_y) not in q:
                    map[new_y, new_x] = True
                    q.append((new_x, new_y))
    
    #print_map(map)

    print(map.sum())
    

def part_2():
    file = "input.txt"
    edges = [(0, 0)]
    #m = {"R": "0", "D": "1", "L": "2", "U": "3"}
    edge_len = 0
    for line in open(file):
        hex_distance, direction = line.strip()[-7:-2], line.strip()[-2:-1]
        distance = int(hex_distance, 16)
        #distance = int(line.split()[1])
        #direction = m[line.split()[0]]

        edge_len += distance

        x, y = edges[-1]
        if direction == "0":
            # right
            edges.append((x+distance, y))
        elif direction == "1":
            # down
            edges.append((x, y+distance))
        elif direction == "2":
            # left
            edges.append((x-distance, y))
        elif direction == "3":
            # up
            edges.append((x, y-distance))
        else:
            raise RuntimeError()

    xs = sorted(set([x for x, y in edges]))
    ys = sorted(set([y for x, y in edges]))

    height = len(ys)-1
    width = len(xs)-1

    tiles = np.zeros((height, width), dtype=bool)

    horizontal_bars = np.zeros((height+1, width), dtype=bool)
    vertical_bars = np.zeros((height+1, width+1), dtype=bool)
    for (from_x, from_y), (to_x, to_y) in zip(edges[:-1], edges[1:]):
        from_x_idx = xs.index(from_x)
        from_y_idx = ys.index(from_y)
        to_x_idx = xs.index(to_x)
        to_y_idx = ys.index(to_y)

        for x in range(min(from_x_idx, to_x_idx), max(from_x_idx, to_x_idx)):
            horizontal_bars[from_y_idx, x] = True

        for y in range(min(from_y_idx, to_y_idx), max(from_y_idx, to_y_idx)):
            vertical_bars[y, from_x_idx] = True

    # dfs to fill all inside tiles
    visited = set()
    q = [(xs.index(0), ys.index(0))]
    while len(q) > 0:
        x, y = q.pop()

        visited.add((x, y))
        tiles[y, x] = True

         # check up
        if y > 0 and not horizontal_bars[y, x] and (x, y-1) not in visited:
            q.append((x, y-1))
        # check down
        if y < height-1 and not horizontal_bars[y+1, x] and (x, y+1) not in visited:
            q.append((x, y+1))
        # check left
        if x > 0 and not vertical_bars[y, x] and (x-1, y) not in visited:
            q.append((x-1, y))
        # check right
        if x < width-1 and not vertical_bars[y, x+1] and (x+1, y) not in visited:
            q.append((x+1, y))


    tot = 0 # edge_len
    for y in range(tiles.shape[0]):
        for x in range(tiles.shape[1]):
            if tiles[y, x]:
                w = xs[x+1] - xs[x] 
                h = ys[y+1] - ys[y] 
                if x == width-1 or not tiles[y, x+1]:
                    w += 1
                    if y > 0 and x+1 <= width-1 and tiles[y-1, x+1]:
                        tot -= 1
                if y == height-1 or not tiles[y+1, x]:
                    h += 1
                tot += w*h

    print(tot)


if __name__ == "__main__":
    part_2()