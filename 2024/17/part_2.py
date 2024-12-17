
class Computer:

    def __init__(self, register, program):
        self.register = register
        self.program = program

        self.ptr = 0
        self.stdout = []

        self.opcodes = [
            self.adv,
            self.bxl,
            self.bst,
            self.jnz,
            self.bxc,
            self.out,
            self.bdv,
            self.cdv
        ]

    def get_combo_operand(self, val: int):
        if val <= 3:
            return val
        elif val == 4:
            return self.register["A"]
        elif val == 5:
            return self.register["B"]
        elif val == 6:
            return self.register["C"]
        else:
            raise RuntimeError()


    def adv(self, arg: int):
        num = self.register["A"]
        denom = 2**self.get_combo_operand(arg)
        res = num // denom
        self.register["A"] = res

    def bxl(self, arg: int):
        self.register["B"] = self.register["B"] ^ arg

    def bst(self, arg: int):
        self.register["B"] = self.get_combo_operand(arg) % 8

    def jnz(self, arg: int):
        if self.register["A"] == 0:
            return
        self.ptr = arg - 2 # TODO. check!

    def bxc(self, arg: int):
        self.register["B"] = self.register["B"] ^ self.register["C"]

    def out(self, arg: int):
        self.stdout.append(self.get_combo_operand(arg) % 8)

    def bdv(self, arg: int):
        num = self.register["A"]
        denom = 2**self.get_combo_operand(arg)
        res = num // denom
        self.register["B"] = res

    def cdv(self, arg: int):
        num = self.register["A"]
        denom = 2**self.get_combo_operand(arg)
        res = num // denom
        self.register["C"] = res

    def run(self, verbose=False):
        while self.ptr < len(self.program):
            if verbose:
                print()
                print(self.register)
                print(f"Executing: {self.program[self.ptr]} {self.program[self.ptr+1]}")

            self.opcodes[self.program[self.ptr]](self.program[self.ptr+1])
            self.ptr += 2

        return self.stdout


def common_beginning(lst1, lst2):
    for i in range(min(len(lst1), len(lst2))):
        if lst1[i] != lst2[i]:
            break
    else:
        i+=1
    return lst1[:i]


program = [2,4,1,3,7,5,1,5,0,3,4,3,5,5,3,0]

prev = 0

prev_diffs = {}

# keep it running for ~20min or so
for i in range(int(1e10)):

    num = 2707053 + 4194304*i

    sample = Computer(
        register={
            "A": num,
            "B": 0,
            "C": 0
        },
        program=program
    )
    res = sample.run()

    if len(cb := common_beginning(program, res)) >= 14:
        print(f"Trying {num}   (diff to prev: {num-prev})")
        print(res)
        print(cb)
        print(program)
        print()
        prev = num

        if num-prev in prev_diffs:
            pass

        prev_diffs[num-prev] = (prev, num)
    if res == program:
        print(num)
        exit(0)

# Input
# register = {
#     "A": 47006051,
#     "B": 0,
#     "C": 0
# }
# program = [2,4,1,3,7,5,1,5,0,3,4,3,5,5,3,0]
