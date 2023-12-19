from heapq import heappop, heappush
from collections import defaultdict
from functools import partial
import numpy as np

# A*

def l1_heuristic(start_pos, end_pos):
    return abs(start_pos[0]-end_pos[0]) + abs(start_pos[1]-end_pos[0])


def part_1():
    file = "input.txt"
    width = len(open(file).readline().strip())
    height = len(open(file).readlines())
    map = np.array([[int(n) for n in row.strip()] for row in open(file)])

    h = partial(l1_heuristic, end_pos=(width-1, height-1))

    q = []  # (f_score, x, y, direction, num_steps)
    heappush(q, (0, 0, 0, "right", 0))
    came_from = {}
    g_score = defaultdict(lambda: np.inf)
    g_score[(0, 0, "right", 0)] = 0

    f_score = defaultdict(lambda: np.inf)
    f_score[(0, 0, "right", 0)] = h((0, 0))

    while len(q) > 0:
        current_fscore, x, y, direction, num_steps = heappop(q)
        if (x, y) == (width-1, height-1):
            return g_score[(x, y, direction, num_steps)]
        
        # enumerate neighbours
        neighbours = []
        if direction in ("right", "left"):
            neighbours += ["up", "down"]
        else:
            neighbours += ["left", "right"]
        if num_steps < 3:
            neighbours.append(direction)

        for next_direction in neighbours:
            next_y = y + 1 if next_direction == "down" else y - 1 if next_direction == "up" else y
            next_x = x + 1 if next_direction == "right" else x - 1 if next_direction == "left" else x

            if not (0 <= next_x < width) or not (0 <= next_y < height):
                continue

            neighbour = (next_x, next_y, next_direction, num_steps + 1 if next_direction == direction else 1)
            tentative_g_score = g_score[(x, y, direction, num_steps)] + map[next_y, next_x]
            if tentative_g_score < g_score[neighbour]:
                # This path is better than any previous one, replace
                came_from[neighbour] = (x, y, direction, num_steps)
                g_score[neighbour] = tentative_g_score
                new_f_score = tentative_g_score + h((next_x, next_y))
                f_score[neighbour] = new_f_score
                if neighbour not in q:
                    heappush(q, (new_f_score, ) + neighbour)


def part_2():
    file = "input.txt"
    width = len(open(file).readline().strip())
    height = len(open(file).readlines())
    map = np.array([[int(n) for n in row.strip()] for row in open(file)])

    h = partial(l1_heuristic, end_pos=(width-1, height-1))

    q = []  # (f_score, x, y, direction, num_steps)
    heappush(q, (0, 0, 0, "right", 0))
    heappush(q, (0, 0, 0, "down", 0))
    came_from = {}
    g_score = defaultdict(lambda: np.inf)
    g_score[(0, 0, "right", 0)] = 0
    g_score[(0, 0, "down", 0)] = 0

    f_score = defaultdict(lambda: np.inf)
    f_score[(0, 0, "right", 0)] = h((0, 0))
    f_score[(0, 0, "down", 0)] = h((0, 0))

    while len(q) > 0:
        current_fscore, x, y, direction, num_steps = heappop(q)
        if (x, y) == (width-1, height-1) and num_steps >= 4:
            return g_score[(x, y, direction, num_steps)]
        
        # enumerate neighbours
        neighbours = []
        if num_steps < 4:
            neighbours = [direction]
        elif num_steps == 10:
            if direction in ("right", "left"):
                neighbours = ["up", "down"]
            else:
                neighbours = ["left", "right"]
        else:
            if direction in ("right", "left"):
                neighbours = [direction] + ["up", "down"]
            else:
                neighbours = [direction] + ["left", "right"]

        for next_direction in neighbours:
            next_y = y + 1 if next_direction == "down" else y - 1 if next_direction == "up" else y
            next_x = x + 1 if next_direction == "right" else x - 1 if next_direction == "left" else x

            if not (0 <= next_x < width) or not (0 <= next_y < height):
                continue

            neighbour = (next_x, next_y, next_direction, num_steps + 1 if next_direction == direction else 1)
            tentative_g_score = g_score[(x, y, direction, num_steps)] + map[next_y, next_x]
            if tentative_g_score < g_score[neighbour]:
                # This path is better than any previous one, replace
                came_from[neighbour] = (x, y, direction, num_steps)
                g_score[neighbour] = tentative_g_score
                new_f_score = tentative_g_score + h((next_x, next_y))
                f_score[neighbour] = new_f_score
                if neighbour not in q:
                    heappush(q, (new_f_score, ) + neighbour)


if __name__ == "__main__":
    print(part_2())