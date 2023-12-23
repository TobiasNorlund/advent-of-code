from queue import Queue
import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)

def part_1():
    map = [line.strip() for line in open("input.txt")]
    side = len(map) 
    
    def max_length(pos, visited: set) -> int:
        visited.add(pos)
        x, y = pos

        if pos == (side-2, side-1):
            return len(visited) -1

        alts = []
        if x+1 < side and map[y][x+1] in (".", ">") and (x+1, y) not in visited:
            l = max_length((x+1, y), visited.copy())
            if l is not None:
                alts.append(l)
        if x-1 >= 0 and map[y][x-1] in (".", "<") and (x-1, y) not in visited:
            l = max_length((x-1, y), visited.copy())
            if l is not None:
                alts.append(l)
        if y+1 < side and map[y+1][x] in (".", "v") and (x, y+1) not in visited:
            l = max_length((x, y+1), visited.copy())
            if l is not None:
                alts.append(l)
        if y-1 >= 0 and map[y-1][x] in (".", "^") and (x, y-1) not in visited:
            l = max_length((x, y-1), visited.copy())
            if l is not None:
                alts.append(l)

        return max(alts) if len(alts) > 0 else None

    print(max_length((1, 0), set()))


def part_2_brute():
    map = [line.strip() for line in open("input.txt")]
    side = len(map) 
    
    def max_length(pos, visited: set) -> int:
        visited.add(pos)
        x, y = pos

        if len(visited) % 1000 == 0:
            print(len(visited))

        if pos == (side-2, side-1):
            return len(visited) -1

        alts = []
        if map[y][x+1] in (".", "<", ">", "v", "^") and (x+1, y) not in visited:
            l = max_length((x+1, y), visited.copy())
            if l is not None:
                alts.append(l)
        if map[y][x-1] in (".", "<", ">", "v", "^") and (x-1, y) not in visited:
            l = max_length((x-1, y), visited.copy())
            if l is not None:
                alts.append(l)
        if map[y+1][x] in (".", "<", ">", "v", "^") and (x, y+1) not in visited:
            l = max_length((x, y+1), visited.copy())
            if l is not None:
                alts.append(l)
        if map[y-1][x] in (".", "<", ">", "v", "^") and (x, y-1) not in visited:
            l = max_length((x, y-1), visited.copy())
            if l is not None:
                alts.append(l)

        return max(alts) if len(alts) > 0 else None

    print(max_length((1, 0), set()))


def part_2():
    map = [line.strip() for line in open("sample.txt")]
    side = len(map)
    valid = (".", "<", ">", "v", "^")

    g = defaultdict(dict) # (x, y): {dir: (x, y, length)}

    def search(x, y, from_dir, num_steps) -> int:
        # check if we're at a branch point
        dirs = []
        if (x, y) == (side-2, side-1):
            return x, y, from_dir, num_steps
        
        if map[y][x+1] in valid and from_dir != "R":
            dirs.append((x+1, y, "L"))
        if map[y][x-1] in valid and from_dir != "L":
            dirs.append((x-1, y, "R"))
        if map[y+1][x] in valid and from_dir != "D":
            dirs.append((x, y+1, "U"))
        if map[y-1][x] in valid and from_dir != "U":
            dirs.append((x, y-1, "D"))
        
        if len(dirs) > 1:
            return x, y, from_dir, num_steps
        else:
            return search(x=dirs[0][0], y=dirs[0][1], from_dir=dirs[0][2], num_steps=num_steps+1)

    # find all branch points and where they lead
    q = Queue()
    q.put((1, 0, "D"))
    while not q.empty():
        x, y, dir = q.get()

        if dir == "R":
            new_x, new_y, from_dir, length = search(x+1, y, "L", 1)
        elif dir == "L":
            new_x, new_y, from_dir, length = search(x-1, y, "R", 1)
        elif dir == "D":
            new_x, new_y, from_dir, length = search(x, y+1, "U", 1)
        elif dir == "U":
            new_x, new_y, from_dir, length = search(x, y-1, "D", 1)
        
        g[(x, y)][dir] = (new_x, new_y, length)
        g[(new_x, new_y)][from_dir] = (x, y, length)

        if (new_x, new_y) == (side-2, side-1):
            # goal state - no other path form here
            continue

        # check branches from new pos that are not already visited
        if "R" not in g[(new_x, new_y)] and map[new_y][new_x+1] in valid:
            q.put((new_x, new_y, "R"))
        if "L" not in g[(new_x, new_y)] and map[new_y][new_x-1] in valid:
            q.put((new_x, new_y, "L"))
        if "D" not in g[(new_x, new_y)] and map[new_y+1][new_x] in valid:
            q.put((new_x, new_y, "D"))
        if "U" not in g[(new_x, new_y)] and map[new_y-1][new_x] in valid:
            q.put((new_x, new_y, "U"))

    # print(len(g.keys()))

    def max_length(x, y, visited, dist):
        if (x, y) == (side-2, side-1):
            return dist
        
        visited.add((x, y))
        alts = []
        for _, (new_x, new_y, length) in g[(x, y)].items():
            if (new_x, new_y) not in visited:
                l = max_length(new_x, new_y, visited.copy(), dist+length)
                if l is not None:
                    alts.append(l)
        
        if len(alts) > 0:
            return max(alts)
        else:
            return None
        
    print(max_length(1, 0, set(), 0))




if __name__ == "__main__":
    part_2()