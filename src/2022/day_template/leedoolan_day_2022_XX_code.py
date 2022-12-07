########## begin ##########
# pylint: disable=unused-variable, import-error

########## global imports ##########
from mylib.general import read_file_into_var, get_file_path

########## global vars ##########
testing = True

########## classes & functions ##########
def get_input_file_data(testing):
    input_file = f"{get_file_path(__file__)}/{'input_example.txt' if testing else 'input.txt'}"
    return read_file_into_var(input_file)


def solve(input_file_data):
    input_data = input_file_data.splitlines()

    part_one = None
    part_two = None
    return (part_one, part_two)


########## main ##########
def main():
    s = solve(get_input_file_data(testing))

    print(f"Part 1 - Answer: {s[0]}")
    print(f"Part 2 - Answer: {s[1]}")


if __name__ == "__main__":
    main()

########## complete ##########
