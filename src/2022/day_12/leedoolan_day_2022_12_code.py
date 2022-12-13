########## begin ##########
# pylint: disable=unused-variable, import-error

########## global imports ##########
from mylib.general import read_file_into_var, get_file_path

########## global vars ##########
testing = False

neighbour_incrs = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}

########## classes & functions ##########
def get_input_file_data(testing):
    input_file = (
        f"{get_file_path(__file__)}/{'input_example.txt' if testing else 'input.txt'}"
    )
    return read_file_into_var(input_file)


class Grid:
    def __init__(self, input_file_data: str = ""):
        x_lines = input_file_data.splitlines()
        self.x_size, self.y_size = len(x_lines[0]), len(x_lines)

        self.grid = [
            [x_lines[y][x] for y in range(self.y_size)] for x in range(self.x_size)
        ]

        self.start = self.find_chars("S")[0]
        self.end = self.find_chars("E")[0]
        self.grid[self.start[0]][self.start[1]] = "a"
        self.grid[self.end[0]][self.end[1]] = "z"

    def print(self):
        for y in range(self.y_size):
            print("".join([self.grid[x][y] for x in range(self.x_size)]))

    def find_chars(self, ch):
        r = []
        for nx, x in enumerate(self.grid):
            for ny, y in enumerate(x):
                if y == ch:
                    r.append((nx, ny))
        return r

    def get_neighbours(self, coord):
        r = []
        coord_val = ord(self.grid[coord[0]][coord[1]]) - 96
        for n in neighbour_incrs.values():  # loop thru possible neighbour squares
            nx, ny = coord[0] + n[0], coord[1] + n[1]
            if -1 < nx < self.x_size and -1 < ny < self.y_size:  # within grid
                if ord(self.grid[nx][ny]) - 96 <= coord_val + 1:  # elevation check
                    r.append((nx, ny))
        return r

    def do_breadth_first_search(self, start, end):
        frontier = [start]
        came_from = {start: None}

        while not len(frontier) == 0:
            current = frontier.pop(0)

            if current == end:
                break

            for next in self.get_neighbours(current):
                if next not in came_from:
                    frontier.append(next)
                    came_from[next] = current

        # build the shortest path
        current = end
        path = []
        while current != start:
            path.append(current)
            current = came_from[current]

        return path


def solve(input_file_data):
    g = Grid(input_file_data)

    part_one = len(g.do_breadth_first_search(g.start, g.end))

    len_paths = []
    for a in g.find_chars("a"):
        # bug here, dont know why but get right answer????
        try:
            len_paths.append(len(g.do_breadth_first_search(a, g.end)))
        except:
            print(a)
    part_two = min(len_paths)

    return (part_one, part_two)


########## main ##########
def main():
    s = solve(get_input_file_data(testing))

    print(f"Part 1 - Answer: {s[0]}")
    print(f"Part 2 - Answer: {s[1]}")


if __name__ == "__main__":
    main()

########## complete ##########
