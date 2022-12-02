########## begin ##########
# pylint: disable=unused-variable, import-error

########## global imports ##########
import os
from mylib.general import read_file_into_var

########## global vars ##########
input_file_name = "input_example.txt"
input_file_path = (
    f"{os.path.dirname(os.path.realpath(__file__))}/{input_file_name}"
)

########## classes & functions ##########
class Grid_Space:
    def __init__(self, contents: str = "."):
        self.contents = contents


class Grid:
    def __init__(self, starting_contents: str = ""):
        x_lines = starting_contents.splitlines()
        self.x_size, self.y_size = len(x_lines[0]), len(x_lines)

        self.grid = [
            [Grid_Space(x_lines[y][x]) for x in range(self.x_size)]
            for y in range(self.y_size)
        ]

    def print(self):
        for y in range(self.y_size):
            print(
                "".join([self.grid[y][x].contents for x in range(self.x_size)])
            )

    def move_both_herds_to_stand_still(self):
        self.move_both_herd_attempts = 0
        while g.move_both_herds():
            pass

    def move_both_herds(self):
        self.move_both_herd_attempts += 1
        moves_done = 0
        for herd in [">", "v"]:
            moves_done += self.move_herd(herd)
        if moves_done > 0:
            return True
        else:
            return False

    def move_herd(self, herd: str):
        moves_done = 0
        possible_moves = [
            [(x, y), self._get_possible_move_position(x, y)]
            for x in range(self.x_size)
            for y in range(self.y_size)
        ]
        possible_moves = [p for p in possible_moves if p[1]]
        for p in possible_moves:
            [(x, y), (x_move, y_move)] = p
            if self.grid[y][x].contents == herd:
                moves_done += 1
                self.move_sea_cucumber(x, y, x_move, y_move)
        return moves_done

    def move_sea_cucumber(
        self, x: int, y: int, x_move: int = None, y_move: int = None
    ):
        s = self.grid[y][x]

        if not x_move or not y_move:
            (x_move, y_move) = self._get_possible_move_position(x, y)

        s_move = self.grid[y_move][x_move]
        s.contents, s_move.contents = ".", s.contents

    def _get_possible_move_position(self, x: int, y: int):
        # get grid space, and return if no contents to move
        s = self.grid[y][x]
        if s.contents == ".":
            return None

        # determine sea cucumber type & get next respective move to space
        if s.contents == ">":
            x_move = (x + 1) if (x + 1) < self.x_size else 0
            y_move = y
        elif s.contents == "v":
            y_move = (y + 1) if (y + 1) < self.y_size else 0
            x_move = x
        s_move = self.grid[y_move][x_move]

        # return move if possible
        if s_move.contents == ".":
            return (x_move, y_move)
        else:
            return None


########## main ##########
# get & parse input data
starting_contents = read_file_into_var(input_file_path)

# set up grid
g = Grid(starting_contents)

# PART 1
g.move_both_herds_to_stand_still()
print(f"No of turns before cannot go: {g.move_both_herd_attempts}")

########## complete ##########
