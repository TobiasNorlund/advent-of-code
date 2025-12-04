M = []  
with open("sample.txt") as f:
    for line in f:
        M.append([c for c in line.strip()])

print(M)

H, W = len(M), len(M[0])

s = 0
for y in range(H):
    for x in range(W):
        m = 0
        # nw
        if 0 <= y-1 and 0 <= x-1 and M[y-1][x-1] == "@":
            m += 1
        # n
        if 0 <= y-1 and M[y-1][x] == "@":
            m += 1
        # ne
        if 0 <= y-1 and 0 <= x+1 < W and M[y-1][x+1] == "@":
            m += 1
        # w
        if 0 <= y < H and 0 <= x-1 < W and M[y][x-1] == "@":
            m += 1
        # e
        if 0 <= y < H and 0 <= x+1 < W and M[y][x+1] == "@":
            m += 1
        # sw
        if 0 <= y+1 < H and 0 <= x-1 < W and M[y+1][x-1] == "@":
            m += 1
        # s
        if 0 <= y+1 < H and 0 <= x < W and M[y+1][x] == "@":
            m += 1
        # se
        if 0 <= y+1 < H and 0 <= x+1 < W and M[y+1][x+1] == "@":
            m += 1
        
        if m < 4 and M[y][x] == "@":
            s += 1
    
print(s)