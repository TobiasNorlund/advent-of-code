ranges = []
nums = []
with open("input.txt") as f:
    for line in f:
        if line == "\n":
            break
            
        start, end = line.strip().split("-")
        ranges.append(range(int(start), int(end)+1))

    for line in f:
        nums.append(int(line.strip()))

print(ranges)
print(nums)

num_fresh = 0
for num in nums:
    for r in ranges:
        if num in r:
            num_fresh += 1
            break

print(num_fresh)