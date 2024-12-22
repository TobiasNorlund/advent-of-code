from collections import defaultdict

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


def get_price(n):
    return int(str(n)[-1])


"""
Strategy:
go through all change sequences of all buyers, and log the total price for each

dp[buyer_i][change_seq] = # total price for this change_seq and all buyers up to this one
"""

dp = [defaultdict(lambda: 0)]

for buyer_i, num in enumerate(init_numbers):

    dp.append(dp[-1].copy())
    visited = set()

    changes = tuple()
    prev_price = get_price(num)
    for i in range(2000):
        num = next_secret_number(num)
        price = get_price(num)
        change = price-prev_price
        if len(changes) < 4:
            changes = changes + (change,)
        else:
            changes = changes[1:] + (change,)
        
        if len(changes) == 4:
            # only update on the first hit for each buyer
            if changes not in visited:
                dp[buyer_i+1][changes] = dp[buyer_i][changes] + price
                visited.add(changes)

        prev_price = price

max_tot_price = max(dp[-1].values())
print(max_tot_price)
