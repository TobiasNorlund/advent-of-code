from functools import lru_cache

with open("input.txt") as f:
    inp = f.read().strip().split()


for step in range(75):

    i = -1
    while (i := i + 1) < len(inp):
        print(i)

        if inp[i] == "0":
            inp[i] = "1"
        elif len(inp[i]) % 2 == 0:
            n1, n2 = str(int(inp[i][:len(inp[i])//2])), str(int(inp[i][len(inp[i])//2:]))
            inp[i] = n1
            inp.insert(i+1, n2)
            i+=1
        else:
            inp[i] = str(int(inp[i]) * 2024)
    
    print(f"Step {step}:")
    print(len(inp))
    print()


print(len(inp))