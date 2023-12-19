import numpy as np
from tqdm import tqdm

def print_map(map):
    for row in map:
        print("".join(row))


def part_1():
    file = "input.txt"
    height = len(open(file).readlines())
    width = len(open(file).readline().strip())

    map = [[c for c in line.strip()] for line in open(file)]

    for x in range(width):
        next_y = 0
        for y in range(height):
            if map[y][x] == "#":
                next_y = y+1
            elif map[y][x] == "O":
                # move this O to next_y
                if next_y < y:
                    map[next_y][x] = "O"
                    map[y][x] = "."
                next_y += 1
    
    tot = 0
    for i, row in zip(reversed(range(1, height+1)), map):
        tot += i * sum(1 for c in row if c == "O")
    print(tot)


def part_2():
    file = "input.txt"
    height = len(open(file).readlines())
    width = len(open(file).readline().strip())

    map = [[c for c in line.strip()] for line in open(file)]

    cache = {}

    for cycle in tqdm(range(120)):#6)):

        # Roll north
        for x in range(width):
            next_y = 0
            for y in range(height):
                if map[y][x] == "#":
                    next_y = y+1
                elif map[y][x] == "O":
                    # move this O to next_y
                    if next_y < y:
                        map[next_y][x] = "O"
                        map[y][x] = "."
                    next_y += 1

        # Roll west
        for y in range(height):
            next_x = 0
            for x in range(width):
                if map[y][x] == "#":
                    next_x = x+1
                elif map[y][x] == "O":
                    # move this O to next_y
                    if next_x < x:
                        map[y][next_x] = "O"
                        map[y][x] = "."
                    next_x += 1

        # Roll south
        for x in range(width):
            next_y = height-1
            for y in reversed(range(height)):
                if map[y][x] == "#":
                    next_y = y-1
                elif map[y][x] == "O":
                    # move this O to next_y
                    if next_y > y:
                        map[next_y][x] = "O"
                        map[y][x] = "."
                    next_y -= 1

        # Roll east
        for y in range(height):
            next_x = width-1
            for x in reversed(range(width)):
                if map[y][x] == "#":
                    next_x = x-1
                elif map[y][x] == "O":
                    # move this O to next_y
                    if next_x > x:
                        map[y][next_x] = "O"
                        map[y][x] = "."
                    next_x -= 1

        #map_str = "\n".join("".join(row) for row in map)
        #if map_str in cache:
        #    print(cycle, cache[map_str], (cycle-130) % 22 + 108)
        #else:
        #    cache[map_str] = cycle

    tot = 0
    for i, row in zip(reversed(range(1, height+1)), map):
        tot += i * sum(1 for c in row if c == "O")
    print(tot)

if __name__ == "__main__":
    part_2()