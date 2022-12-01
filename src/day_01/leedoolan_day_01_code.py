########## begin ##########
# pylint: disable=unused-variable, import-error

########## global imports ##########
import os

########## global vars ##########

########## classes & functions ##########
def read_file_into_var(path, read_as_string=True, encoding="utf-8"):
    """
    This reads a given file into a variable.
    :param path string e.g. "/folder1/file"
    :return string
    """
    txt = ""
    try:
        with open(path, "r", encoding=encoding) as file:
            txt = file.read()
    except Exception as e:
        print(e)

    return txt


########## main ##########
# get input data
input_data_path = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"
input_data = read_file_into_var(input_data_path)

# parse input data
groups_data_raw = input_data.split("\n\n")
groups_data_clean = [x.split("\n") for x in groups_data_raw]

# find totals per group, and reverse sort
totals = [sum(int(y) for y in x) for x in groups_data_clean]
totals = sorted(totals, reverse=True)

# PART 1
print(f"Max Total is: {sum(x for x in [totals[0]])}")

# PART 2
print(f"Total of top 3: {sum(x for x in totals[0:3])}")

########## complete ##########
