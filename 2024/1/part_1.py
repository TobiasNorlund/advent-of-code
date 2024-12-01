

file = "input.txt"

lst_1 = []
lst_2 = []

with open(file) as f:
    for line in f:
        d1, d2 = line.split()
        lst_1.append(int(d1))
        lst_2.append(int(d2))

lst_1 = sorted(lst_1)
lst_2 = sorted(lst_2)

sum_diff = sum(abs(a - b) for a, b in zip(lst_1, lst_2))

print(sum_diff)