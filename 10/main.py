import numpy as np
import matplotlib.pyplot as plt


def step(x, y, dir):
    if dir == "up":
        return x, y-1
    elif dir == "right":
        return x+1, y
    elif dir == "down":
        return x, y+1
    else:
        return x-1, y


def part_1():
    map = [row.strip() for row in open("input.txt").readlines()]
    # find S
    for y, row in enumerate(map):
        if "S" in row:
            start_pos = (row.index("S"), y)
            break

    path = [start_pos + ("up",)]
    #path = [start_pos + ("down",)]
    while True:
        prev_x, prev_y, prev_dir = path[-1]
        cur_x, cur_y = step(prev_x, prev_y, prev_dir)

        if map[cur_y][cur_x] == "S":
            break

        if prev_dir == "up":
            if map[cur_y][cur_x] == "|":
                path.append((cur_x, cur_y, "up"))
            elif map[cur_y][cur_x] == "F":
                path.append((cur_x, cur_y, "right"))
            elif map[cur_y][cur_x] == "7":
                path.append((cur_x, cur_y, "left"))
        elif prev_dir == "down":
            if map[cur_y][cur_x] == "|":
                path.append((cur_x, cur_y, "down"))
            elif map[cur_y][cur_x] == "L":
                path.append((cur_x, cur_y, "right"))
            elif map[cur_y][cur_x] == "J":
                path.append((cur_x, cur_y, "left"))
        elif prev_dir == "right":
            if map[cur_y][cur_x] == "-":
                path.append((cur_x, cur_y, "right"))
            elif map[cur_y][cur_x] == "7":
                path.append((cur_x, cur_y, "down"))
            elif map[cur_y][cur_x] == "J":
                path.append((cur_x, cur_y, "up"))
        elif prev_dir == "left":
            if map[cur_y][cur_x] == "-":
                path.append((cur_x, cur_y, "left"))
            elif map[cur_y][cur_x] == "L":
                path.append((cur_x, cur_y, "up"))
            elif map[cur_y][cur_x] == "F":
                path.append((cur_x, cur_y, "down"))
        else:
            raise RuntimeError()
        
    print(len(path) // 2)

    return path


def part_2():
    map = [row.strip() for row in open("input.txt").readlines()]
    path = part_1()

    height, width = len(map), len(map[0])
    print(path)

    path_tiles = np.zeros((len(map), len(map[0])), dtype=bool)
    for x, y, _ in path:
        path_tiles[y, x] = 1
    plt.imshow(path_tiles, cmap='Greys',  interpolation='nearest')
    plt.show()

    # 1. Starting in top-left corner. Do DFS over all edges to find all "out" vertices
    # 2. Using out vertices, compute all "out" tiles
    # 3. Subtract out and path tiles to find all in tiles

    out_vertices = np.zeros((height+1, width+1), dtype=bool)
    visited = set()
    stack = [(0, 0)]

    def add_to_stack(point):
        if point not in stack and point not in visited:
            stack.append(point)

    def print_map():
        img = np.zeros(((height+1)*10, (width+1) * 10), dtype=bool)
        for y in range(out_vertices.shape[0]):
            for x in range(out_vertices.shape[1]):
                img[y*10, x*10] = out_vertices[y, x]
        plt.imshow(img, cmap='Greys',  interpolation='nearest')
        plt.show()

    while len(stack) > 0:
        y, x = stack.pop()
        visited.add((y, x))
        out_vertices[y, x] = True

        #print(stack)
        #print(y, x)
        #print()
        #print_map()

        # check if we can move right from here
        #  if we're on the edge it is ok
        #  if any of the two neighbouring tiles are non-path tiles, it is ok
        #  if both neighbouring tiles are path, check if we can cross

        # right to (y, x+1)
        if y in (0, height) and x < width:
            # if we're on the edge it is ok
            add_to_stack((y, x+1))
        elif x == width:
            pass
        else:
            if not path_tiles[y-1, x] or not path_tiles[y, x]:
                # if any of the two neighbouring tiles are non-path tiles, it is ok
                add_to_stack((y, x+1))
            else:
                # if both neighbouring tiles are path, check if we can cross
                if not (map[y-1][x] in ("|", "7", "F") or map[y][x] in ("|", "L", "J")):
                    add_to_stack((y, x+1))
        
        # left to (y, x-1)
        if y in (0, height) and x > 0:
            # if we're on the edge it is ok
            add_to_stack((y, x-1))
        elif x == 0:
            pass
        else:
            if not path_tiles[y-1, x-1] or not path_tiles[y, x-1]:
                # if any of the two neighbouring tiles are non-path tiles, it is ok
                stack.append((y, x-1))
            else:
                # if both neighbouring tiles are path, check if we can cross
                if not (map[y-1][x-1] in ("|", "7", "F") or map[y][x-1] in ("|", "L", "J")):
                    stack.append((y, x-1))

        # down to (y+1, x)
        if x in (0, width) and y < height:
            # if we're on the edge it is ok
            add_to_stack((y+1, x))
        elif y == height:
            pass
        else:
            if not path_tiles[y, x-1] or not path_tiles[y, x]:
                # if any of the two neighbouring tiles are non-path tiles, it is ok
                add_to_stack((y+1, x))
            else:
                # if both neighbouring tiles are path, check if we can cross
                if not (map[y][x-1] in ("-", "L", "F") or map[y][x] in ("-", "7", "J")):
                    add_to_stack((y+1, x))

        # up to (y-1, x)
        if x in (0, width) and y > 0:
            # if we're on the edge it is ok
            add_to_stack((y-1, x))
        elif y == 0:
            pass
        else:
            if not path_tiles[y-1, x-1] or not path_tiles[y-1, x]:
                # if any of the two neighbouring tiles are non-path tiles, it is ok
                add_to_stack((y-1, x))
            else:
                # if both neighbouring tiles are path, check if we can cross
                if not (map[y-1][x-1] in ("-", "L", "F") or map[y-1][x] in ("-", "7", "J")):
                    add_to_stack((y-1, x))

    out_tiles = np.zeros((height, width), dtype=bool)
    for y in range(height):
        for x in range(width):
            out_tiles[y, x] = out_vertices[y, x] and out_vertices[y, x+1] and out_vertices[y+1, x] and out_vertices[y+1, x+1]
    print(width * height - (out_tiles + path_tiles).sum())
    plt.imshow(out_tiles + path_tiles, cmap='Greys',  interpolation='nearest')
    plt.show()


if __name__ == "__main__":
    part_2()
