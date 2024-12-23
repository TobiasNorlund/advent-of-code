from itertools import combinations

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = set()

nodes = {}


def get_node(name) -> Node:
    if name not in nodes:
        nodes[name] = Node(name)
    return nodes[name]

with open("input.txt") as f:
    for line in f:
        n1, n2 = line.strip().split("-")
        n1 = get_node(n1)
        n2 = get_node(n2)
        n1.neighbors.add(n2)
        n2.neighbors.add(n1)


def find_common_neighbor(group):
    node = group[0]
    rest = group[1:]
    for neighbor in node.neighbors:
        if neighbor not in rest and all(neighbor in other.neighbors for other in rest):
            return neighbor
        
    return None


groups = []
for n1, n2, n3 in combinations(nodes.values(), r=3):
    if n2 in n1.neighbors and n3 in n1.neighbors and n2 in n3.neighbors:
        groups.append([n1, n2, n3])

for group in groups:
    while (neighbor := find_common_neighbor(group)) is not None:
        group.append(neighbor)


max_len = max(len(g) for g in groups)
longest = [g for g in groups if len(g) == max_len][0]
print(",".join(sorted(n.name for n in longest)))
