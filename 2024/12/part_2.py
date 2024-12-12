from queue import Queue

map = []
with open("input.txt") as f:
    for y, line in enumerate(f):
        map.append([c for c in line.strip()])

h = y+1
w = len(map[0])

plot_to_region = {}
regions = []

def dfs(node, cur_char, cur_region: set):
    y, x = node
    if not (0 <= y < h and 0 <= x < w):
        return set()
    if map[y][x] != cur_char:
        return set()
    
    cur_region.add(node)
    plot_to_region[node] = cur_region

    # Add from all other neighbors
    if (y, x+1) not in plot_to_region and (ns := dfs((y, x+1), cur_char, cur_region)):
        cur_region = cur_region.union(ns)
    if (y, x-1) not in plot_to_region and (ns := dfs((y, x-1), cur_char, cur_region)):
        cur_region = cur_region.union(ns)
    if (y+1, x) not in plot_to_region and (ns := dfs((y+1, x), cur_char, cur_region)):
        cur_region = cur_region.union(ns)
    if (y-1, x) not in plot_to_region and (ns := dfs((y-1, x), cur_char, cur_region)):
        cur_region = cur_region.union(ns)

    return cur_region

for y in range(h):
    for x in range(w):
        if (y, x) not in plot_to_region:
            region = dfs((y, x), map[y][x], set())
            regions.append(region)


def same_side(node_and_dir, perims):
    if node_and_dir not in perims:
        return []
    
    y, x, orientation, dir = node_and_dir
    # remove node_and_dir
    for i in range(len(perims)):
        if perims[i] == node_and_dir:
            del perims[i]
            break

    if orientation == "h":
        # check left & right
        return [node_and_dir] + same_side((y, x+1, "h", dir), perims) + same_side((y, x-1, "h", dir), perims)
    elif orientation == "v":
        return [node_and_dir] + same_side((y+1, x, "v", dir), perims) + same_side((y-1, x, "v", dir), perims)


# compute n sides
prices = 0
for region in regions:
    perims = []
    for y, x in region:
        if (y+1, x) not in region:
            perims.append((y+1, x, "h", "u"))
        if (y-1, x) not in region:
            perims.append((y, x, "h", "l"))
        if (y, x+1) not in region:
            perims.append((y, x+1, "v", "r"))
        if (y, x-1) not in region:
            perims.append((y, x, "v", "l"))

    # count sides
    sides = []
    while len(perims) > 0:
        side = same_side(perims[0], perims)
        sides.append(side)

    prices += len(region) * len(sides)

    #--- debug
    #char = next(iter(region))
    #print(f"{map[char[0]][char[1]]} - price {len(region)} * {len(sides)} = {len(region) * len(sides)}")
    # ---

print(prices)