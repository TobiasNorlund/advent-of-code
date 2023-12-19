from typing import List
import re


def part_1(arr: List[str]):

    numbers = []

    for i, line in enumerate(arr):
        start_idx = -1
        end_idx = -1
        for j, char in enumerate(line):
            if char.isdigit():
                end_idx = j
                if start_idx == -1:
                    start_idx = j
            if (not char.isdigit() or j == len(line)-1) and start_idx > -1:
                end_idx += 1
                numbers.append((int(line[start_idx:end_idx]), range(start_idx, end_idx), i))
                start_idx = -1
                end_idx = -1

    tot = 0
    for n, r, i in numbers:
        pos = [(i-1, j) for j in range(r.start-1, r.stop+1)]
        pos.append((i, r.start-1))
        pos.append((i, r.stop))
        pos += [(i+1, j) for j in range(r.start-1, r.stop+1)]

        for y, x in pos:
            if not 0 <= y < len(arr) or not 0 <= x < len(arr[0]):
                continue
            elif arr[y][x] != "." and not arr[y][x].isdigit():
                tot += n
                break

    return tot


def part_2(arr):
    numbers = []
    stars = []

    for i, line in enumerate(arr):
        for m in re.finditer("\d+", line):
            numbers.append((i,) + m.span())

        for m in re.finditer("\*", line):
            stars.append((i, m.span()[0]))
    
    tot = 0
    for i, j in stars:
        # check if there are exactly two numbers adjacent
        neighbours = []
        for row, start, stop in numbers:
            if (row == i + 1 and j in range(start-1, stop+1)) or \
                (row == i and j in (start-1, stop)) or \
                (row == i - 1 and j in range(start-1, stop+1)):

                neighbours.append(int(arr[row][start:stop]))

        if len(neighbours) == 2:
            #print(neighbours[0], neighbours[1])
            tot += neighbours[0] * neighbours[1]

    return tot


if __name__ == "__main__":
    arr = [line.strip() for line in open("3/input.txt").readlines()]

    # arr = [
    #     "467..114..",
    #     "...*......",
    #     "..35..633.",
    #     "......#...",
    #     "617*......",
    #     "..45.+.58.",
    #     "..592.....",
    #     "......755.",
    #     "...$.*....",
    #     ".664.598.."
    # ]

    #print("Part 1:")
    #print(part_1(arr))
    #print()
    print("Part 2:")
    print(part_2(arr))