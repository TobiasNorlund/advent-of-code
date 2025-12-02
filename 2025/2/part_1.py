with open("input.txt") as f:
    s = f.read().strip()
    ranges = []
    for r in s.split(","):
        start, end = r.split("-")
        ranges.append(range(int(start), int(end)+1))


def is_id_invalid(id: int):
    id_str = str(id)
    mid = len(id_str) // 2
    return len(id_str) % 2 == 0 and id_str[:mid] == id_str[mid:]


s = 0
for r in ranges:
    for id in r:
        if is_id_invalid(id):
            s += id
            #print(id)

print(s)