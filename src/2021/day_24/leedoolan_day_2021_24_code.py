########## begin ##########
# pylint: disable=unused-variable, import-errorunusable tbh

# brute force method - very slow &

########## global imports ##########
import os
from mylib.general import read_file_into_var, process_items

########## global vars ##########
testing = False
input_file_name = "input_example.txt" if testing else "input.txt"
input_file_path = (
    f"{os.path.dirname(os.path.realpath(__file__))}/{input_file_name}"
)

########## classes & functions ##########
class ALU:
    def __init__(self, instructions):
        self.instructions = instructions

    def find_valid_model_no(
        self, model_no_ascend_flag: bool = False, model_no_max_chars=14
    ):
        self.model_no_ascend_flag = model_no_ascend_flag
        self.model_no_max_chars = model_no_max_chars
        self.model_no = "".join(
            [
                "1" if model_no_ascend_flag else "9"
                for x in range(self.model_no_max_chars)
            ]
        )

        while True:
            self.process_model_no()
            if self.z == 0:
                print(f"Found valid model no!")
                self.print()
                break
            else:
                self.get_next_model_no(model_no_ascend_flag)

    def test(self, model_no_max_chars=14):
        self.model_no_max_chars = model_no_max_chars
        _n = "".join(["1" for x in range(self.model_no_max_chars)])

        _i = int(_n)
        _j = _i + 10000  # 00
        self.model_nos = [
            process_model_no(self.instructions, x)
            for x in range(_i, _j, 1)
            if "0" not in str(x)
        ]
        process_items(self.model_nos, lambda x: x.process())

    def reset_alu(self):
        self.inp_index = 0
        self.w, self.x, self.y, self.z = 0, 0, 0, 0

    def get_next_model_no(self, model_no_ascend_flag):
        # vars
        _model_no = int(self.model_no)
        _i = 1 if self.model_no_ascend_flag else -1
        while True:
            _model_no += _i
            if "0" in str(_model_no):
                continue
            else:
                # reset alu
                self.model_no = str(_model_no)
                break

    def print(self):
        print(
            f"model={self.model_no} w={self.w} x={self.x} y={self.y} z={self.z}"
        )


class process_model_no:
    def __init__(self, instructions, model_no):
        self.model_no = model_no
        self.instructions = instructions

    def process(self):
        print(f"Processing model no {self.model_no} . . .")
        self.inp_index = 0
        self.w, self.x, self.y, self.z = 0, 0, 0, 0

        for i in self.instructions:
            op, *params = i.split(" ")
            if len(params) == 2:
                if params[1].isalpha():
                    params[1] = eval(f"int(self.{params[1]})")
                cmd = f"self.{op}('{params[0]}', {params[1]})"
            else:
                cmd = f"self.{op}('{params[0]}')"

            exec(cmd)

    def inp(self, p1):
        exec(f"self.{p1} = str(self.model_no)[self.inp_index]")
        self.inp_index += 1

    def add(self, p1, p2):
        exec(f"self.{p1} += {p2}")

    def mul(self, p1, p2):
        exec(f"self.{p1} *= {p2}")

    def div(self, p1, p2):
        exec(f"self.{p1} = int(int(self.{p1}) / {p2})")

    def mod(self, p1, p2):
        exec(f"self.{p1} = int(int(self.{p1}) % {p2})")

    def eql(self, p1, p2):
        exec(f"self.{p1} = 1 if int(self.{p1})=={p2} else 0")


########## main ##########
# get & parse input data
instructions = read_file_into_var(input_file_path).splitlines()

# set up ALU
a = ALU(instructions)

# PART 1
# a.find_valid_model_no()

a.test(model_no_max_chars=14)


########## complete ##########
