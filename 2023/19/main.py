import re
from dataclasses import dataclass
from numpy import prod

def parse(file):
    workflows = {}
    tools = []
    for line in open(file):
        if m := re.match(r"(?P<name>\w+){(?P<rules>.*)}", line.strip()):
            name = m["name"]
            rules = []
            for rule in m["rules"].split(","):
                if ":" in rule:
                    var, op, num, res = re.match(r"(\w)([<>])(\d+):(\w+)", rule).groups()
                    rules.append((var, op, int(num), res))
                else:
                    rules.append(rule)

            workflows[name] = rules
        elif line.startswith("{"):
            d = {}
            for a in line.strip()[1:-1].split(","):
                var, val = a.split("=")
                d[var] = int(val)
            tools.append(d)

    return workflows, tools


def part_1():
    file = "input.txt"
    workflows, tools = parse(file)

    def search(workflow, tool):
        if workflow == "A":
            return "A"
        elif workflow == "R":
            return "R"

        for rule in workflows[workflow]:
            if type(rule) is str:
                return search(rule, tool)
            else:
                var, op, num, res = rule
                
                if op == ">" and tool[var] > num:
                    return search(res, tool)
                elif op == "<" and tool[var] < num:
                    return search(res, tool)
                else:
                    # does not meet this condition, continue with next rule
                    pass    
        else:
            raise RuntimeError()

    tot = 0
    for tool in tools:
        if search("in", tool) == "A":
            tot += sum(num for _, num in tool.items())

    print(tot)


def invert_rule(var, op, num):
    if op == ">":
        return var, "<", num+1
    else:
        return var, ">", num-1



@dataclass
class RangeCondition:
    start: int
    end: int  # inclusive


def part_2():
    file = "input.txt"
    workflows, _ = parse(file)

    # walk through all paths of the tree starting at "in"
    # record each branches' conditions
    # only keep accepted branches in the end
    # each set of branch conditions should be reducible to one range each for each variable

    accept_conditions = []

    def walk(workflow, conditions: list):
        if workflow == "A":
            accept_conditions.append(conditions)
            return
        elif workflow == "R":
            return

        for rule in workflows[workflow]:
            if type(rule) is str:
                walk(rule, conditions)
            else:
                var, op, num, res = rule

                # add "meet rule" branch
                walk(res, conditions + [(var, op, num)])

                # add "does not meet rule" branch
                conditions.append(invert_rule(var, op, num))

    walk("in", [])

    tot = 0
    for acc_condition in accept_conditions:
        ranges = {v: RangeCondition(1, 4000) for v in ["x", "m", "a", "s"]}

        for condition in acc_condition:
            var, op, num = condition
            if op == "<" and ranges[var].end >= num-1:
                ranges[var].end = num-1
            elif op == ">" and ranges[var].start < num+1:
                ranges[var].start = num+1

        tot += prod([r.end - r.start + 1 for _, r in ranges.items()])

    print(tot)


if __name__ == "__main__":
    part_2()