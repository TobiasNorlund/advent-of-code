from collections import Counter, defaultdict
from functools import cmp_to_key


class_to_rank = {
    "high_card": 1,
    "one_pair": 2,
    "two_pair": 3,
    "three_of_a_kind": 4,
    "full_house": 5,
    "four_of_a_kind": 6,
    "five_of_a_kind": 7
}

class_rank = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 0,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1
}


def class_of(hand: str):
    c = Counter(hand)
    
    c_inv = defaultdict(lambda: [])
    for k, v in c.items():
        if k != "J":
            c_inv[v].append(k)

    # classfiy
    if len(c_inv[5]) == 1 or c["J"] == 5 or (len(c_inv[4]) == 1 and c["J"] == 1) or (len(c_inv[3]) == 1 and c["J"] == 2) or (len(c_inv[2]) == 1 and c["J"] == 3) or (c["J"] == 4):
        return "five_of_a_kind"
    elif len(c_inv[4]) > 0  or (len(c_inv[3]) == 1 and c["J"] == 1) or (len(c_inv[2]) == 1 and c["J"] == 2):
        return "four_of_a_kind"
    elif (len(c_inv[3]) > 0 and len(c_inv[2]) > 0) or (len(c_inv[2]) == 2 and c["J"] == 1):
        return "full_house"
    elif len(c_inv[3]) > 0  or (len(c_inv[2]) == 1 and c["J"] == 1) or (len(c_inv[1]) == 3 and c["J"] == 2):
        return "three_of_a_kind"
    elif len(c_inv[2]) == 2:
        return "two_pair"
    elif len(c_inv[2]) == 1 or (len(c_inv[1]) == 4 and c["J"] == 1):
        return "one_pair"
    else:
        return "high_card"


def sorting_fun(hand_1_and_score, hand_2_and_score):
    hand_1, _ = hand_1_and_score
    hand_2, _ = hand_2_and_score

    hand_1_class = class_of(hand_1)
    hand_2_class = class_of(hand_2)
    if class_to_rank[hand_1_class] > class_to_rank[hand_2_class]:
        return 1
    elif class_to_rank[hand_1_class] < class_to_rank[hand_2_class]:
        return -1
    else:
        # same class
        for i in range(5):
            if class_rank[hand_1[i]] > class_rank[hand_2[i]]:
                return 1
            elif class_rank[hand_1[i]] < class_rank[hand_2[i]]:
                return -1
        return 0


def main():

    hands_and_scores = []
    for line in open("input.txt"):
        hand, score = line.split()
        hands_and_scores.append((hand, int(score)))

    hands_and_scores.sort(key=cmp_to_key(sorting_fun))

    for hand, _ in hands_and_scores:
        print(hand, class_of(hand))

    tot = 0
    for i, (hand, score) in enumerate(hands_and_scores):
        tot += score * (i+1)

    #print(hands_and_scores)
    print(tot)

    

if __name__ == "__main__":
    main()