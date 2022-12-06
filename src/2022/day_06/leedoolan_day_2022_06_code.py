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
def parse_raw_data(input_file_path):
    raw_data = read_file_into_var(input_file_path).splitlines()
    return raw_data


def solve(input_file_path, marker_count):
    raw_data = parse_raw_data(input_file_path)

    word_start = []
    for l in raw_data:
        for n in range(0, len(l) - (marker_count - 1)):
            w = l[n : n + marker_count]
            unique_ch = set(w)
            if len(unique_ch) == marker_count:
                word_start.append(n + marker_count)
                break
    return word_start


########## main ##########
print(f"Part 1 - Answer: {solve(input_file_path, 4)}")
print(f"Part 2 - Answer: {solve(input_file_path, 14)}")

########## complete ##########
