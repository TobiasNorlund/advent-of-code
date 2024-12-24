import re
from collections import defaultdict
from queue import Queue

vals = defaultdict(lambda: None)
nodes = defaultdict(list)

class Node:
    def __init__(self, inp, op, out):
        self.inp1 = inp[0]
        self.inp2 = inp[1]
        self.op = op
        self.out = out

    def compute(self):
        if vals[self.inp1] is not None and vals[self.inp2] is not None:
            vals[self.out] = {
                "XOR": vals[self.inp1] ^ vals[self.inp2],
                "OR": vals[self.inp1] or vals[self.inp2],
                "AND": vals[self.inp1] and vals[self.inp2],
            }[self.op]
            return True
        return False
        
    def __repr__(self):
        return f"<Node out={self.out}>"
        

with open("input.txt") as f:
    read_vals = True
    for line in f:
        if line == "\n":
            read_vals = False
            continue

        if read_vals:
            name, val = re.match(r"(\w+): ([0-1])", line.strip()).groups()
            vals[name] = bool(int(val))
        else:
            n1, op, n2, n3 = re.match(r"(\w+) (\w+) (\w+) -> (\w+)", line.strip()).groups()
            n = Node([n1, n2], op, n3)
            nodes[n1].append(n)
            nodes[n2].append(n)


q = Queue()
for inp in set(nodes.keys()):
    for n in nodes[inp]:
        if n.compute():
            for out in nodes[n.out]:
                q.put(n)


while not q.empty():
    node = q.get()
    if node.compute():
        for n in nodes[node.out]:
            q.put(n)

bits = [vals[f"z{d:02d}"]  for d in range(46)]
dec = sum(2**i*bit for i, bit in enumerate(bits))
print(dec)