ranges = []
nums = []
with open("input.txt") as f:
    for line in f:
        if line == "\n":
            break
            
        start, end = line.strip().split("-")
        ranges.append(range(int(start), int(end)+1))


def range_overlap(r1, r2):
    # if overlap
    if r2.stop <= r1.start or r2.start >= r1.stop:
        return False
    else:
        return True

def range_subtract(r1, r2):
    # returns r1 - r2

    if r2.stop <= r1.start:
        return [r1]
    elif r2.start >= r1.stop:
        return [r1]
    elif r2.start <= r1.start and r2.stop >= r1.stop:
        return []
    elif r2.start <= r1.start and r2.stop < r1.stop:
        # take right end of r1
        return [range(r2.stop, r1.stop)]
    elif r2.start > r1.start and r2.stop >= r1.stop:
        # take left end of r1
        return [range(r1.start, r2.start)]
    else:
        return [
            range(r1.start, r2.start),
            range(r2.stop, r1.stop)
        ]

non_overlapping_ranges = []
for new_range in ranges:

    new_ranges = [new_range]
    for r in non_overlapping_ranges:
        i = 0
        while i < len(new_ranges):
            r2 = new_ranges[i]
            if range_overlap(r, r2):
                # cull the intersecting parts of r2 and replace into new_ranges
                new_ranges[i:i+1] = range_subtract(r2, r)
            else:
                i += 1
    non_overlapping_ranges += new_ranges

s = 0
for r in non_overlapping_ranges:
    s += r.stop - r.start

print(s)