from dataclasses import dataclass


@dataclass
class Position:
    y: int
    x: int

    def __hash__(self):
        return hash((self.y, self.x))

class Box(Position):
    pass

class Stone(Position):
    pass


directions = []
boxes = []
stones = []
with open("input.txt") as f:
    read_dirs = False
    for y, line in enumerate(f):
        if line == "\n":
            read_dirs = True
            h = y
            continue

        if not read_dirs:
            w = len(line.strip()) * 2
            for x, c in enumerate(line.strip()):
                if c == "O":
                    boxes.append(Box(y=y, x=x*2))
                elif c == "#":
                    stones.append(Stone(y=y, x=x*2))
            if "@" in line:
                cur_y = y
                cur_x = line.index("@") * 2
        else:
            directions += [c for c in line.strip()]

#print(h, w)

#h, w = len(m), len(m[0])


def is_pos_occupied(y, x):
    if Box(y, x) in boxes:
        return boxes[boxes.index(Box(y, x))]
    elif Box(y, x-1) in boxes:
        return boxes[boxes.index(Box(y, x-1))]
    elif Stone(y, x) in stones:
        return stones[stones.index(Stone(y, x))]
    elif Stone(y, x-1) in stones:
        return stones[stones.index(Stone(y, x-1))]
    else:
        return None


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
    

def get_boxes_to_push(y, x, dir) -> list:
    if (obj := is_pos_occupied(y, x)) is not None:
        if isinstance(obj, Stone):
            return [None]  # Signal we can't move
        elif isinstance(obj, Box):
            next_y, next_x = get_next_pos_in_dir(obj.y, obj.x, dir)
            if dir == ">":
                next_x += 1
            # elif dir == "<":
            #     next_x -= 1
            ret = [obj] + get_boxes_to_push(next_y, next_x, dir)
            # if we're moving up or down, check obj's second neighbor pos
            if dir in ("^", "v"):
                ret += get_boxes_to_push(next_y, next_x+1, dir)
            return ret
    else:
        return []

    
def print_map():
    m = [["." for _ in range(w)] for _ in range(h)]
    for box in boxes:
        m[box.y][box.x] = "["
        m[box.y][box.x+1] = "]"
    for stone in stones:
        m[stone.y][stone.x] = "#"
        m[stone.y][stone.x+1] = "#"

    m[cur_y][cur_x] = "@"

    for line in m:
        print("".join(line))
    

for i, step_dir in enumerate(directions):

    #print(f"Step {i}: {step_dir}")
    #print_map()
    #print()
    
    y, x = get_next_pos_in_dir(cur_y, cur_x, step_dir)
    bs = get_boxes_to_push(y, x, step_dir)
    bs = set(bs)
    
    if not any(b is None for b in bs):
        # Let's move all these boxes!
        for box in bs:
            next_y, next_x = get_next_pos_in_dir(box.y, box.x, step_dir)
            box.y = next_y
            box.x = next_x
        
        cur_y = y
        cur_x = x

print(f"Final")
print_map()
print()

s = 0
for box in boxes:
    s += box.y*100 + box.x

print(s)