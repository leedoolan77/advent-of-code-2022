########## begin ##########
# pylint: disable=unused-variable, import-error

# Nicked this from https://gist.github.com/AdibSurani/c047a0f0d3d9bc294337cb58da16173e#file-aoc2021_day24-py-L1
# Will try and understand / utilise at some point

########## global imports ##########
import os
from mylib.general import read_file_into_var, process_items
from z3 import *

########## global vars ##########
testing = False
input_file_name = "input_example.txt" if testing else "input.txt"
input_file_path = (
    f"{os.path.dirname(os.path.realpath(__file__))}/{input_file_name}"
)

# each block of code is identical, except for the parameters on lines 4, 5, and 15, so we cache these
lst = open(input_file_path, "r").read().splitlines()
lst = [
    [int(y.split()[-1]) for y in [lst[i + 4], lst[i + 5], lst[i + 15]]]
    for i in range(0, len(lst), 18)
]


def solve(max):
    s = Optimize()
    z = 0  # this is our running z, which has to be zero at the start and end
    v = 0  # this is the value from concatenating our digits
    for (i, [p, q, r]) in enumerate(lst):
        w = Int(f"w{i}")
        v = v * 10 + w
        s.add(And(w >= 1, w <= 9))
        z = If(z % 26 + q == w, z / p, z / p * 26 + w + r)
    s.add(z == 0)

    (s.maximize if max else s.minimize)(v)
    assert s.check() == sat
    return s.model().eval(v)


print(solve(True))  # part 1
print(solve(False))  # part 2
