########## begin ##########
# pylint: disable=unused-variable, import-error

########## global imports ##########
from mylib.general import read_file_into_var, get_file_path

########## global vars ##########
testing = False
sand_start = (500, 0)

########## classes & functions ##########
def get_input_file_data(testing):
    input_file = (
        f"{get_file_path(__file__)}/{'input_example.txt' if testing else 'input.txt'}"
    )
    return read_file_into_var(input_file)


def build_ravine(input_file_data):
    input_data = input_file_data.splitlines()

    lines = []
    for p in input_data:
        pts = p.split(" -> ")
        for n in range(len(pts) - 1):
            lines.append(
                (
                    [int(x) for x in pts[n].split(",")],
                    [int(x) for x in pts[n + 1].split(",")],
                )
            )

    for ([xs, ys], [xe, ye]) in lines:
        xincr = 1 if xs < xe else -1
        yincr = 1 if ys < ye else -1
        for x in range(xs, xe + xincr, xincr):
            for y in range(ys, ye + yincr, yincr):
                fill_space("#", x, y)

    fill_space("+", *sand_start)


def fill_space(c, x, y):
    r[x] = r.get(x, dict())
    r[x][y] = c


def is_blocked(x, y, floor_offset=0):
    if floor_offset > 0:
        if y == max_y + floor_offset:
            return "#"
    return True if return_space(x, y) in ["#", "+", "O"] else False


def return_space(x, y):
    c = "."
    try:
        c = r[x][y]
    except:
        pass
    return c


def drop_sand():
    global max_y, sand_start
    (x, y) = sand_start
    while True and y <= max_y:
        c, bl, b, br = (
            is_blocked(x, y),
            is_blocked(x - 1, y + 1),
            is_blocked(x, y + 1),
            is_blocked(x + 1, y + 1),
        )
        if bl and b and br:
            if c:
                return False
            else:
                fill_space("O", x, y)
                return True
        else:
            y += 1
            if b:
                if bl:
                    x += 1
                else:
                    x -= 1


def drop_sand_floor():
    global max_y, sand_start
    (x, y) = sand_start
    while True:
        c, bl, b, br = (
            is_blocked(x, y, 2),
            is_blocked(x - 1, y + 1, 2),
            is_blocked(x, y + 1, 2),
            is_blocked(x + 1, y + 1, 2),
        )
        if bl and b and br:
            if c:
                return False
            else:
                fill_space("O", x, y)
                return True
        else:
            y += 1
            if b:
                if bl:
                    x += 1
                else:
                    x -= 1


def print_ravine():
    global max_y
    min_x, max_x = min(r), max(r)

    l = ""
    for y in range(0, max_y + 1):
        for x in range(min_x, max_x + 1):
            l += return_space(x, y)
        l += "\n"
    print(l)


def solve(input_file_data):
    global r, max_y

    # part one
    r = dict()
    build_ravine(input_file_data)
    max_y = max([y for v in r.values() for y in v])
    part_one = 0
    while drop_sand():
        part_one += 1

    # part two
    r = dict()
    build_ravine(input_file_data)
    max_y = max([y for v in r.values() for y in v])
    part_two = 0
    while drop_sand_floor():
        part_two += 1
    part_two += 1  # add in one for 500, 0

    return (part_one, part_two)


########## main ##########
def main():
    s = solve(get_input_file_data(testing))

    print(f"Part 1 - Answer: {s[0]}")
    print(f"Part 2 - Answer: {s[1]}")


if __name__ == "__main__":
    main()

########## complete ##########
