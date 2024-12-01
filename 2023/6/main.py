import re

def part_1():
    file = "input.txt"
    times = [int(n) for n in re.findall(r'\d+', list(open(file).readlines())[0])]
    distances = [int(n) for n in re.findall(r'\d+', list(open(file).readlines())[1])]
    
    res = 1
    for time, distance in zip(times, distances):
        num_win_alts = 0
        for hold_time in range(98):
            speed = hold_time
            cand_distance = (time - hold_time) * speed
            if cand_distance > distance:
                num_win_alts += 1

        res *= num_win_alts

    print(res)


def part_2():
    time = 47986698
    distance = 400121310111540

    num_win_alts = 0
    for hold_time in range(time):
        speed = hold_time
        cand_distance = (time - hold_time) * speed
        if cand_distance > distance:
            num_win_alts += 1
    
    print(num_win_alts)


if __name__ == "__main__":
    part_2()