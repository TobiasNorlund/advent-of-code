from typing import List
from tqdm import tqdm
from functools import lru_cache


@lru_cache
def num_arrangements(record: str, sizes: List[int], in_group: bool=False):
    if len(record) == 1:
        if record[0] == ".":
            return 1 if sizes in (tuple(), (0,)) else 0
        elif record[0] == "#":
            return 1 if sizes == (1,) else 0
        else:
            return 1 if sizes in (tuple(), (1,), (0,)) else 0
    
    if record[0] == ".":
        if in_group:
            if sizes[0] != 0:
                return 0
            else:
                return num_arrangements(record[1:], sizes[1:], in_group=False)
        else:
            return num_arrangements(record[1:], sizes, in_group=False)
    elif record[0] == "#":
        if len(sizes) == 0:
            return 0
        elif sizes[0] == 0:
            return 0
        else:
            return num_arrangements(record[1:], (sizes[0]-1,) + sizes[1:] if sizes[0] > 0 else sizes[1:], in_group=True)
    elif record[0] == "?":
        if len(sizes) == 0:
            return num_arrangements(record[1:], sizes)
        else:
            # return sum of ? being either # or .
            if in_group and sizes[0] == 0:
                # can only be "."
                return num_arrangements(record[1:], sizes[1:])
            elif in_group and sizes[0] > 0:
                # can only be #
                return num_arrangements(record[1:], (sizes[0]-1,) + sizes[1:], in_group=True)
            else:
                return (
                    num_arrangements(record[1:], (sizes[0]-1,) + sizes[1:] if sizes[0] > 0 else sizes[1:], in_group=True) + 
                    num_arrangements(record[1:], sizes)
                )


def part_1():
    records = []
    for line in open("input.txt"):
        record, sizes = line.strip().split(" ")
        sizes = [int(n) for n in sizes.split(",")]
        records.append((record, sizes))

    tot = 0
    for record, sizes in records:
        n = num_arrangements(record, sizes)
        # print(n)
        tot += n
        
    print(tot)


def part_2():
    records = []
    for line in open("input.txt"):
        record, sizes = line.strip().split(" ")
        record = "?".join([record for _ in range(5)])
        sizes = tuple(int(n) for n in sizes.split(",")) * 5
        records.append((record, sizes))

    tot = 0
    for record, sizes in tqdm(records):
        tot += num_arrangements(record, sizes)

    print(tot)

    #from multiprocessing import Pool
    #with Pool(20) as p:
    #    res = p.starmap(num_arrangements, tqdm(records))
    #print(sum(res))


if __name__ == "__main__":
    part_2()