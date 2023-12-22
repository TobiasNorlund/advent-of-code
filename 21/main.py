import numpy as np
from queue import Queue
import random


def parse(file):
    map = np.array(
        [
            [c in (".", "S") for c in line.strip()]
            for line in open(file)
        ],
        dtype=bool
    )
    for y, line in enumerate(open(file)):
        for x, c in enumerate(line.strip()):
            if c == "S":
                start_pos = (x, y)

    return map, start_pos

def part_1():
    file = "input.txt"
    map, start_pos = parse(file)

    height, width = map.shape

    q = Queue()
    queued = set()

    def q_put(item):
        if item not in queued:
            q.put(item)
            queued.add(item)

    q_put(start_pos + (0, ))

    term_pos = set()

    while not q.empty():
        x, y, num_steps = q.get()

        if num_steps == 64:
            term_pos.add((x, y))
            continue

        # check up
        if y-1 >= 0 and map[y-1, x]:
            q_put((x, y-1, num_steps+1))
        # check down
        if y+1 < height and map[y+1, x]:
            q_put((x, y+1, num_steps+1))
        # check left
        if x-1 >= 0 and map[y, x-1]:
            q_put((x-1, y, num_steps+1))
        # check right
        if x+1 < width and map[y, x+1]:
            q_put((x+1, y, num_steps+1))

    print(len(term_pos))

    
def get_minimum_steps(map, start_pos):
    height, width = map.shape
    q = Queue()
    queued = set()
    queued.add(start_pos)
    q.put(start_pos + (0, ))
    min_steps = -np.ones((height, width), dtype=np.int32)
    while not q.empty():
        x, y, num_steps = q.get()
        min_steps[y, x] = num_steps
        
        # check up
        if (y-1 >= 0 and map[y-1, x]) and (x, y-1) not in queued:
            q.put((x, y-1, num_steps+1))
            queued.add((x, y-1))
        
        # check down
        if (y+1 < height and map[y+1, x]) and (x, y+1) not in queued:
            q.put((x, y+1, num_steps+1))
            queued.add((x, y+1))
        
        # check left
        if (x-1 >= 0 and map[y, x-1]) and (x-1, y) not in queued:
            q.put((x-1, y, num_steps+1))
            queued.add((x-1, y))
        
        # check right
        if (x+1 < width and map[y, x+1]) and (x+1, y) not in queued:
            q.put((x+1, y, num_steps+1))
            queued.add((x+1, y))
    
    return min_steps


def get_quadrant_tiles(map, start_steps, target_steps, min_steps_from_start):
    side = map.shape[0]
    x_multiple = 0
    y_multiple = 0
    tot_tiles = 0

    cache = {
        0: map[(min_steps_from_start % 2 == 0) & map].sum(),
        1: map[(min_steps_from_start % 2 == 1) & map].sum()
    }

    while start_steps + side * x_multiple -1 < target_steps:
        while True:
            if random.randint(0, 10000) == 0:
                print(x_multiple, y_multiple)

            # num steps to get to bottom left corner
            steps = start_steps + side * (x_multiple + y_multiple)
            even_or_odd = (target_steps + steps) % 2
            if target_steps >= steps + 2*side:
                # we can reach all tiles
                tot_tiles += cache[even_or_odd]
                y_multiple += 1
            elif target_steps >= steps:
                # we can reach some tiles on this map
                rem_steps = target_steps - steps
                tot_tiles += ((min_steps_from_start <= rem_steps) & (min_steps_from_start % 2 == even_or_odd) & map).sum()
                y_multiple += 1
            else:
                # no tiles are reachable, break
                break
        y_multiple = 0
        x_multiple += 1
    
    return tot_tiles


def part_2_brute():
    file = "sample.txt"
    map, start_pos = parse(file)
    height, width = map.shape

    q = Queue()
    queued = set()

    def q_put(item):
        if item not in queued:
            q.put(item)
            queued.add(item)

    q_put(start_pos + (0, ))

    term_pos = set()

    while not q.empty():
        real_x, real_y, num_steps = q.get()
        x = real_x % width
        y = real_y % height
        
        if num_steps == 100:
            term_pos.add((real_x, real_y))
            continue

        # check up
        if (y-1 >= 0 and map[y-1, x]) or (y-1 == -1 and map[height-1, x]):
            q_put((real_x, real_y-1, num_steps+1))
        
        # check down
        if (y+1 < height and map[y+1, x]) or (y+1 == height and map[0, x]):
            q_put((real_x, real_y+1, num_steps+1))
        
        # check left
        if (x-1 >= 0 and map[y, x-1]) or (x-1 == -1 and map[y, width-1]):
            q_put((real_x-1, real_y, num_steps+1))
        
        # check right
        if (x+1 < width and map[y, x+1]) or (x+1 == width and map[y, 0]):
            q_put((real_x+1, real_y, num_steps+1))

    print("upper right quadrant:", sum(1 for x, y in term_pos if x >= width and y < 0))
    print("upper left quadrant:", sum(1 for x, y in term_pos if x < 0 and y < 0))
    print("lower right quadrant:", sum(1 for x, y in term_pos if x >= width and y >= height))
    print("lower left quadrant:", sum(1 for x, y in term_pos if x < 0 and y >= height))
    print("right", sum(1 for x, y in term_pos if x >= width and 0 <= y < height))
    print("left", sum(1 for x, y in term_pos if x < 0 and 0 <= y < height))
    print("up", sum(1 for x, y in term_pos if 0 <= x < width and y < 0))
    print("down", sum(1 for x, y in term_pos if 0 <= x < width and y >= height))

    #a = np.zeros((height, width), dtype=np.int32)
    #for y in range(height):
    #    for x in range(width):
    #        if (x, y) in term_pos:
    #            a[y, x] = 1
    #        #if not map[y, x]:
    #        #    a[y, x] = -1
                
    #center_min_steps = get_minimum_steps(map, (start_pos))
    #print(center_min_steps)
                
    #print(a.sum())

    #print(a)

    print(len(term_pos)) 


def part_2():
    # Not working yet
    file = "input.txt"
    map, start_pos = parse(file)
    side, _ = map.shape

    target_steps = 26501365
    even_or_odd = target_steps % 2

    # start from center - how many minimum steps to get to all tiles?
    center_min_steps = get_minimum_steps(map, (start_pos))
    tot_tiles = map[(center_min_steps % 2 == even_or_odd) & map].sum()

    # QUADRANTS

    # upper right quadrant
    upper_right = get_minimum_steps(map, (0, side-1))
    upper_right_tiles = get_quadrant_tiles(map, center_min_steps[0, -1] + 2, target_steps, upper_right)
    print("uppler right quadrant", upper_right_tiles)

    # upper left quadrant
    upper_left = get_minimum_steps(map, (side-1, side-1))
    upper_left_tiles = get_quadrant_tiles(map, center_min_steps[0, 0] + 2, target_steps, upper_left)
    print("upper left quadrant", upper_left_tiles)

    # lower right quadrant
    lower_right = get_minimum_steps(map, (0, 0))
    lower_right_tiles = get_quadrant_tiles(map, center_min_steps[-1, -1] + 2, target_steps, lower_right)
    print("lower right quadrant", lower_right_tiles)

    # lower left quadrant
    lower_left = get_minimum_steps(map, (side-1, 0))
    lower_left_tiles = get_quadrant_tiles(map, center_min_steps[-1, 0] + 2, target_steps, lower_left)
    print("lower left quadrant", lower_left_tiles)

    tot_tiles += upper_right_tiles + upper_left_tiles + lower_right_tiles + lower_left_tiles

    # STRAIGHT

    # right
    start_steps = center_min_steps[:, -1]
    right_tiles = 0
    while True:
        right_steps = np.minimum.reduce([
            np.where(map, start_steps[y] + 1 + get_minimum_steps(map, (0, y)), -1) for y in range(side)
        ])
        if np.all(right_steps[:, 0] >= target_steps):
            break
        else:
            right_tiles += map[(right_steps <= target_steps) & (right_steps % 2 == even_or_odd) & map].sum()
        start_steps = right_steps[:, -1]
    print("right", right_tiles)

    # left
    start_steps = center_min_steps[:, 0]
    left_tiles = 0
    while True:
        left_steps = np.minimum.reduce([
            np.where(map, start_steps[y] + 1 + get_minimum_steps(map, (side-1, y)), -1) for y in range(side)
        ])
        if np.all(left_steps[:, -1] >= target_steps):
            break
        else:
            left_tiles += map[(left_steps <= target_steps) & (left_steps % 2 == even_or_odd) & map].sum()
        start_steps = left_steps[:, 0]
    print("left", left_tiles)

    # up
    start_steps = center_min_steps[0, :]
    up_tiles = 0
    while True:
        up_steps = np.minimum.reduce([
            np.where(map, start_steps[x] + 1 + get_minimum_steps(map, (x, side-1)), -1) for x in range(side)
        ])
        if np.all(up_steps[-1, :] >= target_steps):
            break
        else:
            up_tiles += map[(up_steps <= target_steps) & (up_steps % 2 == even_or_odd) & map].sum()
        start_steps = up_steps[0, :]
    print("up", up_tiles)

    # down
    start_steps = center_min_steps[-1, :]
    down_tiles = 0
    while True:
        down_steps = np.minimum.reduce([
            np.where(map, start_steps[x] + 1 + get_minimum_steps(map, (x, 0)), -1) for x in range(side)
        ])
        if np.all(down_steps[0, :] >= target_steps):
            break
        else:
            down_tiles += map[(down_steps <= target_steps) & (down_steps % 2 == even_or_odd) & map].sum()
        start_steps = down_steps[-1, :]
    print("down", down_tiles)


    tot_tiles += right_tiles + left_tiles + up_tiles + down_tiles

    print(tot_tiles)


if __name__ == "__main__":
    #part_2_brute()
    part_2()