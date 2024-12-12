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

print(regions)

# compute perimeter
prices = 0
for region in regions:
    perim = 0
    for y, x in region:
        if (y+1, x) not in region:
            perim += 1
        if (y-1, x) not in region:
            perim += 1
        if (y, x+1) not in region:
            perim += 1
        if (y, x-1) not in region:
            perim += 1

    print(perim)
    prices += len(region) * perim

print(prices)