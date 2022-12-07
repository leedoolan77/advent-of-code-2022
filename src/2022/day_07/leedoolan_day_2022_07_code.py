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


def solve(input_file_path):
    raw_data = parse_raw_data(input_file_path)

    dirs = {}
    wd = ""
    for i in raw_data:
        # get working dir
        if i.startswith("$ cd "):
            _dir = i.split("$ cd ")[1]
            if _dir == "/":
                _dir = "root"
            wd = (
                "/".join(wd.split("/")[0:-1])
                if _dir == ".."
                else f"{wd}/{_dir}"
            )
            dirs[wd] = dirs.get(wd, [])

        # get contents and add total
        if i.split(" ")[0].isnumeric():
            dirs[wd].append(int(i.split(" ")[0]))

            # add total in to parent dir total too
            for d in range(2, len(wd.split("/")), 1):
                pd = "/".join(wd.split("/")[0:d])
                dirs[pd].append(int(i.split(" ")[0]))

    dir_totals = {k: int(sum(v)) for k, v in dirs.items()}
    space_req = 30000000 - (70000000 - dir_totals["/root"])

    part_one = sum([x for x in [v for v in dir_totals.values()] if x <= 100000])
    part_two = min([v for v in dir_totals.values() if v >= space_req])
    return (part_one, part_two)


########## main ##########
s = solve(input_file_path)
print(f"Part 1 - Answer: {s[0]}")
print(f"Part 2 - Answer: {s[1]}")

########## complete ##########
