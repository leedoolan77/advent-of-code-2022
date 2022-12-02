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

shape_lk = {"A": "R", "B": "P", "C": "S", "X": "R", "Y": "P", "Z": "S"}
shape_score_lk = {"R": 1, "P": 2, "S": 3}

########## classes & functions ##########
def get_outcome_score(opp, you):
    # draw
    if opp == you:
        return 3

    # wins
    if opp == "R" and you == "P":
        return 6
    if opp == "P" and you == "S":
        return 6
    if opp == "S" and you == "R":
        return 6

    # else loss
    return 0


def get_exp_res_shape(opp, exp_res):
    # draw
    if exp_res == "Y":
        if opp == "A":
            return "X"
        if opp == "B":
            return "Y"
        if opp == "C":
            return "Z"

    # wins
    if exp_res == "Z":
        if opp == "A":
            return "Y"
        if opp == "B":
            return "Z"
        if opp == "C":
            return "X"
    else:  # else loss
        if opp == "A":
            return "Z"
        if opp == "B":
            return "X"
        if opp == "C":
            return "Y"


def get_total_score(part, rounds):
    total_score = 0
    for r in rounds:
        # get opp, you choices
        if part == 1:
            opp, you = r.split(" ")
        else:  # else part two lookup you shape
            opp, exp_res = r.split(" ")
            you = get_exp_res_shape(opp, exp_res)
        opp, you = shape_lk[opp], shape_lk[you]

        # get score
        round_score = shape_score_lk[you] + get_outcome_score(opp, you)
        total_score += round_score

    print(f"Part {part} - Total Score: {total_score}")


########## main ##########
# get & parse input data
rounds = read_file_into_var(input_file_path).splitlines()

# parts
get_total_score(1, rounds)
get_total_score(2, rounds)


########## complete ##########
