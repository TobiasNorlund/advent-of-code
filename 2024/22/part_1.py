
init_numbers = []
with open("input.txt") as f:
    for line in f:
        init_numbers.append(int(line.strip()))


def next_secret_number(n):
    n = (n * 64) ^ n
    n = n % 16777216

    n = (n // 32) ^ n
    n = n % 16777216
    
    n = (n * 2048) ^ n
    n = n % 16777216
    return n


def get_2000th_secret_number(init_num):
    num = init_num
    for _ in range(2000):
        num = next_secret_number(num)
    return num


s = 0
for init_num in init_numbers:
    s += get_2000th_secret_number(init_num)

print(s)