########## begin ##########
# pylint: disable=unused-variable, import-error

########## global imports ##########
import os
from mylib.general import read_file_into_var

########## global vars ##########
input_file_name = "input.txt"
input_file_path = (
    f"{os.path.dirname(os.path.realpath(__file__))}/{input_file_name}"
)

########## classes & functions ##########

########## main ##########
# get input data
input_data = read_file_into_var(input_file_path)

# parse input data
groups_data_raw = input_data.split("\n\n")
groups_data_clean = [x.split("\n") for x in groups_data_raw]

# find totals per group, and reverse sort
totals = [sum(int(y) for y in x if y != "") for x in groups_data_clean]
totals = sorted(totals, reverse=True)

# PART 1
print(f"Max Total is: {sum(x for x in [totals[0]])}")

# PART 2
print(f"Total of top 3: {sum(x for x in totals[0:3])}")

########## complete ##########
