########## begin ##########
# pylint: disable=unused-variable, import-error

########## global imports ##########
import os
from mylib.general import read_file_into_var

########## global vars ##########
testing = False
input_file_name = "input_example.txt" if testing else "input.txt"

input_file_path = (
    f"{os.path.dirname(os.path.realpath(__file__))}/{input_file_name}"
)

########## classes & functions ##########
def get_priority_value(i):
    return ord(i) - (96 if i.islower() else (64 - 26))


def part_one(raw_data):
    # loop thru rucksacks
    priority_total = 0
    for r in raw_data:
        # get rucksack compartment items
        c_size = int(len(r) / 2)
        x, y = r[0:c_size], r[c_size:]

        # check each item in each compartment, stop if found duplicate
        for i in x:
            if i in y:
                priority_total += get_priority_value(i)
                break
    return priority_total


def part_two(raw_data):
    # loop through rucksacks in groups of 3
    priority_total = 0
    for i in range(0, len(raw_data), 3):
        # get each rucksack in group
        x, y, z = raw_data[i], raw_data[i + 1], raw_data[i + 2]

        # check each item in each compartment, stop if found duplicate
        for i in x:
            if i in y and i in z:
                priority_total += get_priority_value(i)
                break
    return priority_total


########## main ##########
# get & parse input data
raw_data = read_file_into_var(input_file_path).splitlines()

# parts
print(f"Part 1 - Priority Total: {part_one(raw_data)}")
print(f"Part 2 - Priority Total: {part_two(raw_data)}")
########## complete ##########
