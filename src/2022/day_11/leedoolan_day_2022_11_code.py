########## begin ##########
# pylint: disable=unused-variable, import-error

########## global imports ##########
from mylib.general import read_file_into_var, get_file_path
import re

########## global vars ##########
testing = False

monkey_parse = r"""Monkey (?P<id>\d+):
  Starting items: (?P<items>.+)
  Operation: new = (?P<op>.+)
  Test: divisible by (?P<test_div>\d+)
    If true: throw to monkey (?P<test_true_monkey>\d+)
    If false: throw to monkey (?P<test_false_monkey>\d+)"""

########## classes & functions ##########
def get_input_file_data(testing):
    input_file = (
        f"{get_file_path(__file__)}/{'input_example.txt' if testing else 'input.txt'}"
    )
    return read_file_into_var(input_file)


class Monkey:
    def __init__(self, raw_data):
        self.__dict__ = re.search(monkey_parse, raw_data).groupdict()
        self.items = eval(f"[{self.items}]")
        self.test_div = int(self.test_div)
        self.test_true_monkey, self.test_false_monkey = int(self.test_true_monkey), int(
            self.test_false_monkey
        )
        self.item_inspections = 0

    def inspect_items(self, worry_divisor=1, common_modulo=1):
        self.item_inspections += len(self.items)
        if worry_divisor == 1:
            self.items = [eval(f"({self.op}) % {common_modulo}") for old in self.items]
        else:
            self.items = [
                int(eval(f"({self.op}) / {worry_divisor}")) for old in self.items
            ]
        _ = [
            monkeys[
                self.test_true_monkey
                if i % self.test_div == 0
                else self.test_false_monkey
            ].items.append(i)
            for i in self.items
        ]
        self.items = []


def solve(input_file_data):
    global monkeys

    # part one
    monkeys = [Monkey(m) for m in input_file_data.split("\n\n")]
    rounds, worry_divisor = 20, 3
    for r in range(rounds):
        for m in monkeys:
            m.inspect_items(worry_divisor=worry_divisor)
    inspections = sorted([m.item_inspections for m in monkeys], reverse=True)
    part_one = inspections[0] * inspections[1]

    # part two
    monkeys = [Monkey(m) for m in input_file_data.split("\n\n")]

    # common modulo created from product of all monkeys test divisors
    rounds, common_modulo = 10000, 1
    for m in monkeys:
        common_modulo *= m.test_div

    for r in range(rounds):
        for m in monkeys:
            m.inspect_items(common_modulo=common_modulo)
    inspections = sorted([m.item_inspections for m in monkeys], reverse=True)
    part_two = inspections[0] * inspections[1]

    return (part_one, part_two)


########## main ##########
def main():
    s = solve(get_input_file_data(testing))

    print(f"Part 1 - Answer: {s[0]}")
    print(f"Part 2 - Answer: {s[1]}")


if __name__ == "__main__":
    main()

########## complete ##########
