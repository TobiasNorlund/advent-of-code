from collections import defaultdict
from itertools import combinations
from queue import Queue
from tqdm import tqdm
from copy import deepcopy
from math import comb


def get_connected_components(g):
    connected_components = []  # set()
    q = set([k for k in g.keys()])

    while len(q) > 0:
        k = q.pop()

        con_com = set()
        nq = Queue()
        nq.put(k)
        while not nq.empty():
            node = nq.get()
            for n in g[node]:
                if n not in con_com:
                    nq.put(n)
                    con_com.add(n)
                    if n in q:
                        q.remove(n)
        connected_components.append(con_com)
    
    return connected_components


def part_1_brute():
    g = defaultdict(list)
    edges = set()
    for line in open("input.txt"):
        a, b = line.strip().split(": ")
        b = b.split()
        for c in b:
            g[a].append(c)
            g[c].append(a)
            edges.add(tuple(sorted((a, c))))

    print(len(edges))

    for edges in tqdm(combinations(edges, 3), total=comb(len(edges), 3)):
        test_g = deepcopy(g)
        for a, b in edges:
            test_g[a].remove(b)
            test_g[b].remove(a)
        con_com = get_connected_components(test_g)
        if len(con_com) > 1:
            print()
            print(edges)
            print(len(con_com[0]) * len(con_com[1]))
            print()
            return
        
def edge(n1, n2):
    return tuple(sorted((n1, n2)))


def shortest_path(n1, n2, g, excluding_edges=set()):
    # bfs
    q = Queue()
    visited = set()
    q.put((n1, [n1]))  # list of nodes passed
    while not q.empty():
        n, path = q.get()
        visited.add(n)
        if n == n2:
            return path
        for nbor in g[n]:
            if nbor not in visited and edge(n, nbor) not in excluding_edges:
                q.put((nbor, path + [nbor]))
    else:
        return None


def part_1():
    g = defaultdict(list)
    edges = set()
    for line in open("input.txt"):
        a, b = line.strip().split(": ")
        b = b.split()
        for c in b:
            g[a].append(c)
            g[c].append(a)
            edges.add(tuple(sorted((a, c))))

    #edges = [('hqq', 'xxq'), ('qfb', 'vkd'), ('kgl', 'xzz')]
    #print(edges)
    #for a, b in edges:
    #    g[a].remove(b)
    #    g[b].remove(a)
    #
    #con_com = get_connected_components(g)
    #print(len(con_com[0]) * len(con_com[1]))  # 514794
    #return
    
    # take an edge
    for n1, n2 in tqdm(edges):
        # get shortest path from n1 to n2, excluding this edge
        path = shortest_path(n1, n2, g, excluding_edges=set([edge(n1, n2)]))
        
        # if this edge is separator, another separator must be in the path
        # for each edge in path, get shortest path excluding both edges
        for m1, m2 in zip(path, path[1:]):
            path2 = shortest_path(m1, m2, g, excluding_edges=set([edge(n1, n2), edge(m1, m2)]))
            # for each edge in that path, check if the two nodes are not connected, in such case, we have our trio
            for o1, o2 in zip(path2, path2[1:]):
                if shortest_path(o1, o2, g, excluding_edges=set([edge(n1, n2), edge(m1, m2), edge(o1, o2)])) is None:
                    # bingo!
                    edges = [edge(n1, n2), edge(m1, m2), edge(o1, o2)]
                    print()
                    print(edges)
                    for a, b in edges:
                        g[a].remove(b)
                        g[b].remove(a)
                    
                    con_com = get_connected_components(g)
                    print(len(con_com[0]) * len(con_com[1]))
                    return
        

if __name__ == "__main__":
    part_1()