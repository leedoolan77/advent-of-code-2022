########## begin ##########
# pylint: disable=unused-variable, import-error

########## global imports ##########
from mylib.general import read_file_into_var, get_file_path

########## global vars ##########
testing = False

########## classes & functions ##########
def get_input_file_data(testing):
    input_file = f"{get_file_path(__file__)}/{'input_example.txt' if testing else 'input.txt'}"
    return read_file_into_var(input_file)


def solve(input_file_data):
    input_data = input_file_data.replace(" ", "\n").splitlines()

    cycles = [0]
    x = 1
    prev_c = ""
    for c in input_data:
        if prev_c == "addx":
            x += int(c)
        cycles.append(x)
        prev_c = c

    crt = ""
    for h in range(0, 221, 40):
        crt += "".join(
            [
                "#" if abs((n - 1) - cycles[n + h - 1]) <= 1 else "."
                for n in range(1, 41)
            ]
        )
        crt += "\n"

    print(crt)

    part_one = sum([cycles[n - 1] * n for n in range(20, 221, 40)])
    part_two = "RFZEKBFA"  # added maually on manual sight!
    return (part_one, part_two)


########## main ##########
def main():
    s = solve(get_input_file_data(testing))

    print(f"Part 1 - Answer: {s[0]}")
    print(f"Part 2 - Answer: {s[1]}")


if __name__ == "__main__":
    main()

########## complete ##########
