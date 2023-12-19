
def HASH(s):
    v = 0
    for c in s:
        v += ord(c)
        v *= 17
        v = v % 256
    return v


def part_1():
    seq = open("input.txt").read().strip().split(",")
    tot = 0
    for s in seq:
        tot += HASH(s)
    print(tot)


def print_boxes(boxes):
    for i, box in enumerate(boxes):
        if len(box) > 0:
            print(f"Box {i}: {box}")


def part_2():
    seq = open("input.txt").read().strip().split(",")
    boxes = [[] for _ in range(256)]

    for s in seq:
        if "-" in s:
            label = s[:-1]
            box = HASH(label)
            for i in range(len(boxes[box])):
                if boxes[box][i][0] == label:
                    del boxes[box][i]
                    break
        else:
            label, num = s.split("=")
            box = HASH(label)
            for i, (old_l, _) in enumerate(boxes[box]):
                if old_l == label:
                    boxes[box][i] = (label, num)
                    break
            else:
                boxes[box].append((label, num))

        #print_boxes(boxes)
        #print()

    tot = 0
    for i in range(256):
        for slot_no, (lbl, num) in enumerate(boxes[i]):
            tot += (i+1) * (slot_no+1) * int(num)
    print(tot)



if __name__ == "__main__":
    part_2()