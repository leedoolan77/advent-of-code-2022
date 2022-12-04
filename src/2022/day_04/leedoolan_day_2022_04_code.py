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
def part_one(raw_data):
    # loop thu pairs, get l/h value of each, and then compare
    fully_contains_total = 0
    for pair in raw_data:
        [l1, h1, l2, h2] = [
            int(x) for p in pair.split(",") for x in p.split("-")
        ]
        if (l1 >= l2 and h1 <= h2) or (l2 >= l1 and h2 <= h1):
            fully_contains_total += 1
    return fully_contains_total


def part_two(raw_data):
    # loop thu pairs, get l/h value of each, and then compare
    overlaps_total = 0
    for pair in raw_data:
        [l1, h1, l2, h2] = [
            int(x) for p in pair.split(",") for x in p.split("-")
        ]
        if (
            (l1 <= l2 <= h1)
            or (l1 <= h2 <= h1)
            or (l2 <= l1 <= h2)
            or (l2 <= h1 <= h2)
        ):
            overlaps_total += 1
    return overlaps_total


########## main ##########
# get & parse input data
raw_data = read_file_into_var(input_file_path).splitlines()

# parts
print(f"Part 1 - Answer: {part_one(raw_data)}")
print(f"Part 2 - Answer: {part_two(raw_data)}")
########## complete ##########
