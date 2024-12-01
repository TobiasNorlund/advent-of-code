import re

def part_1():
    tot = 0
    for line in open("input.txt"):
        nums = re.findall(r'\d+', line)

        winning = [int(n) for n in nums[1:11]]
        tickets = [int(n) for n in nums[11:]]

        n = sum(1 for t in tickets if t in winning)
        if n > 0:
            tot += 2**(n-1)

    print(tot)


def part_2():
    num_cards = len(open("4/input.txt").readlines())
    copies = [1] * num_cards
    for i, line in enumerate(open("4/input.txt")):
        nums = re.findall(r'\d+', line)

        winning = [int(n) for n in nums[1:11]]
        tickets = [int(n) for n in nums[11:]]

        n = sum(1 for t in tickets if t in winning)
        for j in range(i+1, i+1+n):
            if j < len(copies):
                copies[j] += copies[i]
        
    print(sum(copies))


if __name__ == "__main__":
    # part_1()
    part_2()