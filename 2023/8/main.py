import re
from itertools import cycle

def part_1():
    with open("input.txt") as f:
        turns = f.readline().strip()
        f.readline()

        nodes = {}
        for line in f.readlines():
            node, L, R = re.findall(r"[A-Z]{3}", line)
            nodes[node] = {"L": L, "R": R}
    
    cur_node = "AAA"
    for num_steps, turn in enumerate(cycle(turns)):
        cur_node = nodes[cur_node][turn]
        if cur_node == "ZZZ":
            break

    print(num_steps+1)
    

def part_2():
    with open("input.txt") as f:
        turns = f.readline().strip()
        f.readline()

        nodes = {}
        start_nodes = []
        for line in f.readlines():
            node, L, R = re.findall(r"[A-Z1-9]{3}", line)
            nodes[node] = {"L": L, "R": R}
            if node[-1] == "A":
                start_nodes.append(node)

    for start_node in start_nodes:
        node = start_node
        num_steps = 0
        c = 0
        last = None
        for turn in cycle(turns):
            node = nodes[node][turn]
            num_steps += 1
            if node[-1] == "Z":
                print(f"{start_node} -> {node} in {num_steps} steps ({num_steps - last if last else 0} since last)")
                last = num_steps
                c += 1
                if c == 5:
                    break

    print("Look up least common multiple of [20093, 12169, 13301, 20659, 16697, 17263] = 10668805667831 by e.g. prime factorization")


if __name__ == "__main__":
    part_2()

    l = [20092, 12169, 17263, 16697, 20659, 13301]

    s = [set(n * k for k in range(1, 100)) for n in l]
