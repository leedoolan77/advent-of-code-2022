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


class Grid:
    def __init__(self, input_file_data: str = ""):
        x_lines = input_file_data.splitlines()
        self.x_size, self.y_size = len(x_lines[0]), len(x_lines)

        self.grid = [
            [x_lines[x][y] for x in range(self.x_size)]
            for y in range(self.y_size)
        ]

    def print(self):
        for y in range(self.y_size):
            print("".join([self.grid[x][y] for x in range(self.x_size)]))


def solve(input_file_data):
    # build grid of trees, use class as easier to share attrs
    g = Grid(input_file_data)
    if testing:
        g.print()

    # determine scores
    sum_visible_score = g.x_size * 2 + (g.y_size - 2) * 2  # outer trees
    sum_visible_score += sum(
        [
            get_tree_visible_score(g, x, y)
            for x in range(1, g.x_size - 1)
            for y in range(1, g.y_size - 1)
        ]
    )  # inner trees
    max_scenic_score = max(
        [
            get_tree_scenic_score(g, x, y)
            for x in range(1, g.x_size - 1)
            for y in range(1, g.y_size - 1)
        ]
    )  # inner trees

    # return values
    part_one, part_two = sum_visible_score, max_scenic_score
    return (part_one, part_two)


def get_tree_visible_score(g, x, y):
    tr = g.grid[x][y]
    l, r, t, b = True, True, True, True
    xs = [x for x in range(g.x_size)]
    ys = [y for y in range(g.y_size)]

    for n in xs[0:x]:  # check from left
        if g.grid[n][y] >= tr:
            l = False
            break

    for n in xs[x + 1 : g.x_size]:  # check from right
        if g.grid[n][y] >= tr:
            r = False
            break

    for n in ys[0:y]:  # check from top
        if g.grid[x][n] >= tr:
            t = False
            break

    for n in ys[y + 1 : g.y_size]:  # check from bottom
        if g.grid[x][n] >= tr:
            b = False
            break

    return 1 if l or r or t or b else 0


def get_tree_scenic_score(g, x, y):
    tr = g.grid[x][y]
    l, r, t, b = 0, 0, 0, 0
    xs = [x for x in range(g.x_size)]
    ys = [y for y in range(g.y_size)]

    if x > 0:
        for n in xs[0:x][::-1]:  # check to left
            l += 1
            if g.grid[n][y] >= tr:
                break

    if x < g.x_size - 1:
        for n in xs[x + 1 :]:  # check to right
            r += 1
            if g.grid[n][y] >= tr:
                break

    if y > 0:
        for n in ys[0:y][::-1]:  # check to top
            t += 1
            if g.grid[x][n] >= tr:
                break

    if y < g.y_size - 1:
        for n in ys[y + 1 :]:  # check to bottom
            b += 1
            if g.grid[x][n] >= tr:
                break

    scenic_score = l * r * t * b
    if testing:
        print(
            x,
            y,
            tr,
            scenic_score,
            l,
            r,
            t,
            b,
            xs[0:x][::-1],
            xs[x + 1 :],
            ys[0:y][::-1],
            ys[y + 1 :],
        )
    return scenic_score


########## main ##########
def main():
    s = solve(get_input_file_data(testing))

    print(f"Part 1 - Answer: {s[0]}")
    print(f"Part 2 - Answer: {s[1]}")


if __name__ == "__main__":
    main()

########## complete ##########
