import math

with open("input.txt", "r") as f:
    n = 50
    res_counter = 0
    print(n)
    for line in f:
        dir = 1 if line[0] == "R" else -1
        tot_rot = int(line[1:])

        if line[0] == "R":
            passes_0 = (n + tot_rot) // 100
        else:
            passes_0 = abs(math.floor((n - tot_rot) / 100))
            if n == 0:
                passes_0 -= 1

        n = (n + dir * tot_rot) % 100
        res_counter += passes_0
        if line[0] == "L" and n == 0:
            res_counter += 1

        print(line.strip(), res_counter, n)


print("---")
print(res_counter)