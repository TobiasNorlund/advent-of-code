with open("input.txt") as f:
    s = f.read().strip()
    ranges = []
    for r in s.split(","):
        start, end = r.split("-")
        ranges.append(range(int(start), int(end)+1))


def get_divisors(l: int):
    divisors = [i for i in range(1, l) if l % i == 0]
    return divisors


def is_id_invalid(id: int):
    id_str = str(id)
    for div in get_divisors(len(id_str)):
        if len(set([id_str[i:i+div] for i in range(0, len(id_str), div)])) == 1:
            return True
    else:
        return False

s = 0
for r in ranges:
    for id in r:
        if is_id_invalid(id):
            s += id
            print(id)

print(s)