from functools import cache
from tqdm import tqdm
from math import log2

with open("input.txt") as f:
    inp = f.read().strip().split()

@cache
def process_stone(n, rem_steps):
    #print(rem_steps, n)
    if rem_steps == 0:
        return 1

    if n == "0":
        return process_stone("1", rem_steps-1)
    elif len(n) % 2 == 0:
        n1, n2 = str(int(n[:len(n)//2])), str(int(n[len(n)//2:]))
        return process_stone(n1, rem_steps-1) + process_stone(n2, rem_steps-1)
    else:
        return process_stone(str(int(n) * 2024), rem_steps-1)


s = sum(process_stone(n, 75) for n in inp)

print(s)