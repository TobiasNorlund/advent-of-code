with open("input.txt", "r") as f:
    n = 50
    res_counter = 0
    for line in f:
        dir = 1 if line[0] == "R" else -1
        num = int(line[1:])
        n = (n + dir * num) % 100
        print(n)
        if n == 0:
            res_counter += 1

print("---")
print(res_counter)