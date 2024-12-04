
inp = []

with open("input.txt") as f:
    for line in f:
        inp.append(line.strip())


w, h = len(inp[0]), len(inp)

s = 0

for y in range(len(inp)):
    for x in range(len(inp[0])):
        # check l2r
        if inp[y][x:x+4] == "XMAS":
            s += 1
        if inp[y][x-4:x] == "SAMX":
            s += 1
        if inp[y][x] == "X" and \
            y+1 < len(inp) and inp[y+1][x] == "M" and \
            y+2 < len(inp) and inp[y+2][x] == "A" and \
            y+3 < len(inp) and inp[y+3][x] == "S":
            s += 1
        if inp[y][x] == "X" and \
            y-1 >= 0 and inp[y-1][x] == "M" and \
            y-2 >= 0 and inp[y-2][x] == "A" and \
            y-3 >= 0 and inp[y-3][x] == "S":
            s += 1
        # diagonal down right
        if inp[y][x] == "X" and \
            y+1 < h and x+1 < w and inp[y+1][x+1] == "M" and \
            y+2 < h and x+2 < w and inp[y+2][x+2] == "A" and \
            y+3 < h and x+3 < w and inp[y+3][x+3]== "S":
            s += 1
        # diagonal down left
        if inp[y][x] == "X" and \
            y+1 < h and x-1 >= 0 and inp[y+1][x-1] == "M" and \
            y+2 < h and x-2 >= 0 and inp[y+2][x-2] == "A" and \
            y+3 < h and x-3 >= 0 and inp[y+3][x-3]== "S":
            s += 1
        # diagonal up right
        if inp[y][x] == "X" and \
            y-1 >= 0 and x+1 < w and inp[y-1][x+1] == "M" and \
            y-2 >= 0 and x+2 < w and inp[y-2][x+2] == "A" and \
            y-3 >= 0 and x+3 < w and inp[y-3][x+3]== "S":
            s += 1
        # diagonal up left
        if inp[y][x] == "X" and \
            y-1 >= 0 and x-1 >= 0 and inp[y-1][x-1] == "M" and \
            y-2 >= 0 and x-2 >= 0 and inp[y-2][x-2] == "A" and \
            y-3 >= 0 and x-3 >= 0 and inp[y-3][x-3]== "S":
            s += 1

print(s)