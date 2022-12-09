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


class Object:
    def __init__(self):
        self.x, self.y = 0, 0
        self.move_count = 0
        self.visited_xy = [(self.x, self.y)]

        self.incr_moves = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
        self.poss_spaces = [v for v in self.incr_moves.values()] + [
            (x, y) for x in [1, -1] for y in [1, -1]
        ]

    def move(self, direction="", x=0, y=0):
        if direction == "":
            self.x, self.y = x, y
        else:
            self.x += self.incr_moves[direction][0]
            self.y += self.incr_moves[direction][1]
        self.move_count += 1
        self.visited_xy.append((self.x, self.y))

    def catchup(self, target_x, target_y):
        # first check if no catchup required
        if abs(target_x - self.x) <= 1 and abs(target_y - self.y) <= 1:
            return

        # lastly lets loop thru and test possible other moves
        for (incr_x, incr_y) in self.poss_spaces:
            test_x, test_y = (target_x + incr_x), (target_y + incr_y)
            if abs(self.x - test_x) <= 1 and abs(self.y - test_y) <= 1:
                self.move(x=test_x, y=test_y)
                return


def solve(input_file_data):
    input_data = input_file_data.splitlines()

    knot_count = 10
    knots = [Object() for n in range(knot_count)]

    # loop thru instructions
    for i in input_data:
        [direction, moves] = i.split(" ")
        moves = int(moves)
        for _m in range(moves):
            for n in range(knot_count):
                if n == 0:
                    knots[n].move(direction=direction)
                else:
                    knots[n].catchup(knots[n - 1].x, knots[n - 1].y)

    part_one = len(set(knots[1].visited_xy))
    part_two = len(set(knots[9].visited_xy))
    return (part_one, part_two)


########## main ##########
def main():
    s = solve(get_input_file_data(testing))

    print(f"Part 1 - Answer: {s[0]}")
    print(f"Part 2 - Answer: {s[1]}")


if __name__ == "__main__":
    main()

########## complete ##########
