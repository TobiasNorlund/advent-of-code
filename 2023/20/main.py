from queue import Queue
from collections import defaultdict

class Broadcaster:
    def __init__(self, name, outputs: list):
        self.name = name
        self.outputs = outputs
    
    def process(self, input, signal, queue):
        for output in self.outputs:
            queue.put((self.name, output, signal))

class FlipFlopModule:
    def __init__(self, name, outputs: list):
        self.name = name
        self.outputs = outputs
        self.state = False

    def process(self, input, signal, signal_queue: Queue):
        if signal == True:
            return
        else:
            self.state = not self.state
            for output in self.outputs:
                signal_queue.put((self.name, output, self.state))


class ConjunctionModule:
    def __init__(self, name, inputs: list, outputs: list):
        self.name = name
        self.inputs = inputs
        self.states = {i: False for i in inputs}
        self.outputs = outputs

    def process(self, input, signal, signal_queue):
        self.states[input] = signal
        out_signal = not all(v for v in self.states.values())
        for output in self.outputs:
            signal_queue.put((self.name, output, out_signal))


def parse(file):
    modules = {}
    inputs = defaultdict(list)

    # collect inputs
    for line in open(file):
        module, outputs = line.strip().split(" -> ")
        outputs = outputs.split(", ")
        if module[0] in ("%", "&"):
            for output in outputs:
                inputs[output].append(module[1:])
    
    for line in open(file):
        module, outputs = line.strip().split(" -> ")
        outputs = outputs.split(", ")
        if module == "broadcaster":
            modules["broadcaster"] = Broadcaster("broadcaster", outputs=outputs)
        elif module.startswith("%"):
            modules[module[1:]] = FlipFlopModule(module[1:], outputs=outputs)
        else:
            modules[module[1:]] = ConjunctionModule(module[1:], inputs=inputs[module[1:]], outputs=outputs)
        
    return modules


def part_1():
    file = "input.txt"
    modules = parse(file)

    q = Queue()
    num_low = 0
    num_high = 0
    for n in range(1000):
        q.put(("button", "broadcaster", False))
        while not q.empty():
            source, target, signal = q.get()
            if not signal:
                num_low += 1
            else:
                num_high += 1
            #print(f"{source} -{'high' if signal else 'low'}-> {target}")

            if target in modules:
                modules[target].process(source, signal, q)

    print(num_low*num_high)


def part_2():
    file = "input.txt"
    modules = parse(file)

    q = Queue()
    last_high = defaultdict(lambda: 0)
    for n in range(1000000):
        q.put(("button", "broadcaster", False))
        while not q.empty():
            source, target, signal = q.get()

            if source in ("pl", "mz", "lz", "zm") and signal: # and signal == True:
                print(source, n - last_high[source])
                last_high[source] = n

            if target in modules:
                modules[target].process(source, signal, q)

    # Calculate least common multiple of:
    # pl 3796
    # zm 3822
    # mz 3880
    # lz 4002
    # = 225514321828633


if __name__ == "__main__":
    part_2()