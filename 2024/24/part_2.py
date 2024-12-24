import re
from collections import defaultdict

nodes = defaultdict(lambda: None)

SWAPS = {
    "z09": "rkf",
    "rkf": "z09",

    "jgb": "z20",
    "z20": "jgb",

    "vcg": "z24",
    "z24": "vcg",

    "rvc": "rrs",
    "rrs": "rvc"
}

with open("input.txt") as f:
    read_vals = True
    for line in f:
        if line == "\n":
            read_vals = False
            continue

        if not read_vals:
            n1, op, n2, n3 = re.match(r"(\w+) (\w+) (\w+) -> (\w+)", line.strip()).groups()
            if n2.startswith("x"):
                n1, n2 = n2, n1
            nodes[(n1, op, n2)] = n3 if n3 not in SWAPS else SWAPS[n3]


def check_bit(i: int, prev_carry: str) -> str:
    A = nodes[(f"x{i:02d}", "XOR", f"y{i:02d}")]
    B = nodes[(A, "XOR", prev_carry)] or nodes[(prev_carry, "XOR", A)]
    C = nodes[(f"x{i:02d}", "AND", f"y{i:02d}")]
    D = nodes[(A, "AND", prev_carry)] or nodes[(prev_carry, "AND", A)]
    E = nodes[(C, "OR", D)] or nodes[(D, "OR", C)]

    if B is not None and E is not None:
        return E
    else:
        return "ERROR"


next_carry = "mjh"
for i in range(1, 44):
    next_carry = check_bit(i, next_carry)
    if next_carry == "ERROR":
        print("ERROR")
        break
else:
    print(",".join(sorted(SWAPS.keys())))
