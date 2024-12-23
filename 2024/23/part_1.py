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


n_three_groups = 0
for n1, n2, n3 in combinations(nodes.values(), r=3):
    if n2 in n1.neighbors and n3 in n1.neighbors and n2 in n3.neighbors:
        if n1.name.startswith("t") or n2.name.startswith("t") or n3.name.startswith("t"):
            n_three_groups += 1

print(n_three_groups)