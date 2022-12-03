########## begin ##########
# pylint: disable=unused-variable, import-error

########## global imports ##########
import os
from mylib.general import read_file_into_var

########## global vars ##########
testing = True
input_file_name = "example.txt" if testing else "input.txt"

input_file_path = (
    f"{os.path.dirname(os.path.realpath(__file__))}/{input_file_name}"
)

########## classes & functions ##########


########## main ##########
# get & parse input data
raw_data = read_file_into_var(input_file_path).splitlines()

# parts


########## complete ##########
