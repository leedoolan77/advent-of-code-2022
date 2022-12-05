########## begin ##########
# pylint: disable=unused-variable, import-error

########## global imports ##########
import os
from mylib.general import read_file_into_var

########## global vars ##########
testing = True
input_file_name = "input_example.txt" if testing else "input.txt"

input_file_path = (
    f"{os.path.dirname(os.path.realpath(__file__))}/{input_file_name}"
)

########## classes & functions ##########
def parse_data(input_file_path):
    raw_data = read_file_into_var(input_file_path)
    return raw_data


def part_one(raw_data):

    return None


def part_two(raw_data):
    return None


########## main ##########
raw_data = parse_data(input_file_path)

print(f"Part 1 - Answer: {part_one(raw_data)}")
print(f"Part 2 - Answer: {part_two(raw_data)}")
########## complete ##########
