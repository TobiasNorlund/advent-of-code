
# Sample
# register = {
#     "A": 729,
#     "B": 0,
#     "C": 0
# }
# program = [0,1,5,4,3,0]

# Input
register = {
    "A": 47006051,
    "B": 0,
    "C": 0
}
program = [2,4,1,3,7,5,1,5,0,3,4,3,5,5,3,0]


ptr = 0

def get_combo_operand(val: int):
    if val <= 3:
        return val
    elif val == 4:
        return register["A"]
    elif val == 5:
        return register["B"]
    elif val == 6:
        return register["C"]
    else:
        raise RuntimeError()


def adv(arg: int):
    num = register["A"]
    denom = 2**get_combo_operand(arg)
    res = num // denom
    register["A"] = res

def bxl(arg: int):
    register["B"] = register["B"] ^ arg

def bst(arg: int):
    register["B"] = get_combo_operand(arg) % 8

def jnz(arg: int):
    global ptr
    if register["A"] == 0:
        return
    ptr = arg - 2 # TODO. check!

def bxc(arg: int):
    register["B"] = register["B"] ^ register["C"]

def out(arg: int):
    print(get_combo_operand(arg) % 8, end=",")

def bdv(arg: int):
    num = register["A"]
    denom = 2**get_combo_operand(arg)
    res = num // denom
    register["B"] = res

def cdv(arg: int):
    num = register["A"]
    denom = 2**get_combo_operand(arg)
    res = num // denom
    register["C"] = res


opcodes = [
    adv,
    bxl,
    bst,
    jnz,
    bxc,
    out,
    bdv,
    cdv
]


while ptr < len(program):
    #print(register)
    #print(f"Executing: {program[ptr]} {program[ptr+1]}")

    opcodes[program[ptr]](program[ptr+1])
    ptr += 2
    #print()

print()