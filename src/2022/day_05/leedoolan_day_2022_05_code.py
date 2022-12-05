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
def parse_data(input_file_path):
    raw_data = read_file_into_var(input_file_path)
    [crates_raw, moves_raw] = raw_data.split("\n\n")

    # get move in form of array moves, from, to
    moves = []
    for m in moves_raw.splitlines():
        moves.append([int(x) for x in m.split(" ") if x.isnumeric()])

    # build crates as dict of list
    crates = {}
    crates_raw = crates_raw.splitlines()[::-1]  # reverse
    for c in crates_raw[0].split("   "):  # loop through each stack
        c = int(c.strip())
        crates[c] = []
        for l in crates_raw[1:]:
            content = (
                l[((c - 1) * 4) : ((c - 1) * 4) + 3]
                .strip()
                .replace("[", "")
                .replace("]", "")
            )
            if content != "":
                crates[c].append(content)

    return moves, crates


def part_one(input_file_path):
    moves, crates = parse_data(input_file_path)

    for [n, f, t] in moves:
        for x in range(n):
            crates[t].append(
                crates[f].pop()
            )  # pop removes item, but returns val, can do in single operation
    return "".join([v[-1] for v in crates.values()])


def part_two(input_file_path):
    moves, crates = parse_data(input_file_path)

    for [n, f, t] in moves:
        to_move = crates[f][-n:]
        crates[f] = crates[f][0:-n]
        crates[t].extend(to_move)
    return "".join([v[-1] for v in crates.values()])


########## main ##########
print(f"Part 1 - Answer: {part_one(input_file_path)}")
print(f"Part 2 - Answer: {part_two(input_file_path)}")

########## complete ##########
