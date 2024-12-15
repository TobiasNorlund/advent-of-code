
m = []
directions = []
with open("input.txt") as f:
    read_dirs = False
    for y, line in enumerate(f):
        if line == "\n":
            read_dirs = True
            continue

        if not read_dirs:
            m.append([c for c in line.strip()])
            if "@" in line:
                cur_y = y
                cur_x = line.index("@")
        else:
            directions += [c for c in line.strip()]


h, w = len(m), len(m[0])


def get_next_pos_in_dir(y, x, dir):
    if dir == "<":
        return y, x-1
    elif dir == "^":
        return y-1, x
    elif dir == ">":
        return y, x+1
    elif dir == "v":
        return y+1, x
    else:
        raise RuntimeError()
    

def get_line_end_of_boxes(y, x, len, dir):
    if not (0 <= y < h and 0 <= x < w):
        return None

    if m[y][x] == "O":
        y, x = get_next_pos_in_dir(y, x, dir)
        return get_line_end_of_boxes(y, x, len+1, dir)
    elif m[y][x] == "#":
        return None
    elif m[y][x] == ".":
        return y, x, len



def print_map():
    for line in m:
        print("".join(line))
    

for i, step_dir in enumerate(directions):

    print(f"Step {i}: {step_dir}")
    #print_map()
    print()
    
    y, x = get_next_pos_in_dir(cur_y, cur_x, step_dir)
    if (line_end := get_line_end_of_boxes(y, x, 0, step_dir)) is not None:
        y_end, x_end, length = line_end
        if length > 0:
            # If we're pushing boxes, add a box at the end
            m[y_end][x_end] = "O"
        # Move robot
        m[y][x] = "@"
        m[cur_y][cur_x] = "."
        cur_y, cur_x = y, x


s = 0
for y in range(h):
    for x in range(w):
        if m[y][x] == "O":
            s += y*100+x

print(s)