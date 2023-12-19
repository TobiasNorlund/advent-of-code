import numpy as np
from queue import Queue


def part_1(map, start_pos=None):
    height, width = len(map), len(map[0])

    energized = np.zeros((height, width), dtype=bool)
    visited = set()

    q = Queue()
    if start_pos is None:
        q.put((0, 0, "right"))  # x, y, direction
    else:
        q.put(start_pos)

    while not q.empty():
        x, y, direction = q.get()
        if not (0 <= x < width) or not (0 <= y < height):
            continue
        
        if (x, y, direction) in visited:
            continue

        energized[y, x] = True
        visited.add((x, y, direction))

        if map[y][x] == ".":
            next_y = y + 1 if direction == "down" else y - 1 if direction == "up" else y
            next_x = x + 1 if direction == "right" else x - 1 if direction == "left" else x
            q.put((next_x, next_y, direction))
        elif map[y][x] == "/":
            if direction == "up":
                next_x, next_y, next_dir = x+1, y, "right"
            elif direction == "down":
                next_x, next_y, next_dir = x-1, y, "left"
            elif direction == "left":
                next_x, next_y, next_dir = x, y+1, "down"
            elif direction == "right":
                next_x, next_y, next_dir = x, y-1, "up"
            q.put((next_x, next_y, next_dir))
        elif map[y][x] == "\\":
            if direction == "up":
                next_x, next_y, next_dir = x-1, y, "left"
            elif direction == "down":
                next_x, next_y, next_dir = x+1, y, "right"
            elif direction == "left":
                next_x, next_y, next_dir = x, y-1, "up"
            elif direction == "right":
                next_x, next_y, next_dir = x, y+1, "down"
            q.put((next_x, next_y, next_dir))
        elif map[y][x] == "-":
            if direction in ("up", "down"):
                q.put((x-1, y, "left"))
                q.put((x+1, y, "right"))
            else:
                next_y = y
                next_x = x + 1 if direction == "right" else x - 1
                q.put((next_x, next_y, direction))
        elif map[y][x] == "|":
            if direction in ("right", "left"):
                q.put((x, y-1, "up"))
                q.put((x, y+1, "down"))
            else:
                next_y = y + 1 if direction == "down" else y - 1
                next_x = x
                q.put((next_x, next_y, direction))

    return energized.sum()


def part_2(map):
    height, width = len(map), len(map[0])

    maximum = 0

    # top-down and bottom-up
    for x in range(width):
        maximum = max(maximum, part_1(map, start_pos=(x, 0, "down")))
        maximum = max(maximum, part_1(map, start_pos=(x, height-1, "up")))

    for y in range(height):
        maximum = max(maximum, part_1(map, start_pos=(0, y, "right")))
        maximum = max(maximum, part_1(map, start_pos=(width-1, y, "left")))

    return maximum


if __name__ == "__main__":
    file = "input.txt"
    #width = len(open(file).readline().strip())
    #height = len(open(file).readlines())

    map = [row.strip() for row in open(file)]

    print(part_2(map))