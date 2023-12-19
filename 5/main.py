import re


def parse_input(input_file):
    maps = []

    with open(input_file) as f:
        while line := f.readline():
            if line.startswith("seeds:"):
                seeds = [int(n) for n in re.findall(r'\d+', line)]
            
            elif line.endswith("map:\n"):
                ranges = []
                while (line := f.readline()) not in ("\n", ""):
                    nums = [int(n) for n in re.findall(r'\d+', line)]
                    ranges.append((range(nums[1], nums[1] + nums[2]), nums[0]))
                maps.append(ranges)
    
    return seeds, maps


def map_ranges(ranges, num: int):
    # ranges_dict: list of tuples (source range, dest start)
    for source_range, dest_start in ranges:
        if num in source_range:
            return num - source_range.start + dest_start
    else:
        return num


def part_1():
    seeds, maps = parse_input("input.txt")
    min_location = 1e10
    for num in seeds:
        for m in maps:
            num = map_ranges(m, num)
        min_location = min(min_location, num)
    
    print(min_location)


def part_2():
    seeds, maps = parse_input("input.txt")

    seed_ranges = [range(start, start + length) for start, length in zip(seeds[::2], seeds[1::2])]

    min_location = 1e10
    min_seed = None
    min_range = None

    # Start with ends of seed ranges
    for seed_range in seed_ranges:
        seed = seed_range.start
        while seed in seed_range:
            num = seed
            for m in maps:
                num = map_ranges(m, num)
            if num < min_location:
                min_seed = seed
                min_location = num
                min_range = seed_range
                print(min_seed, min_location)
            seed += 1000

    print(f"Candidate range: {min_range}")

    for seed in range(max(min_seed - 1000, min_range.start), min(min_seed + 1000, min_range.stop)):
        num = seed
        for m in maps:
            num = map_ranges(m, num)
        if num < min_location:
            min_location = num

    print(min_location)


if __name__ == "__main__":
    part_2()