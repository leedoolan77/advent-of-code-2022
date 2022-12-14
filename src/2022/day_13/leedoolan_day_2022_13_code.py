########## begin ##########
# pylint: disable=unused-variable, import-error

########## global imports ##########
from mylib.general import read_file_into_var, get_file_path

########## global vars ##########
testing = True

########## classes & functions ##########
def get_input_file_data(testing):
    input_file = (
        f"{get_file_path(__file__)}/{'input_example.txt' if testing else 'input.txt'}"
    )
    return read_file_into_var(input_file)


def compare(l, r):
    if type(l) is int:
        l = [l]
    if type(r) is int:
        r = [r]
    l_len, r_len = len(l), len(r)
    if l_len < r_len:
        return True
    min_l = min([l_len, r_len])
    for i in range(min_l):
        if type(l[i]) is int and type(r[i]) is int:
            if l[i] < r[i]:
                return True
            if l[i] > r[i]:
                return False
        else:
            compare(l[i], r[i])
    return False


def solve(input_file_data):
    input_data = input_file_data.split("\n\n")
    packets = [(eval(p.split("\n")[0]), eval(p.split("\n")[1])) for p in input_data]

    r = []
    for n, p in enumerate(packets):
        r.append((n + 1, compare(*p), p))
    print(r)

    part_one = sum([n + 1 for n, p in enumerate(packets) if compare(*p)])
    part_two = None
    return (part_one, part_two)


########## main ##########
def main():
    s = solve(get_input_file_data(testing))

    print(f"Part 1 - Answer: {s[0]}")
    print(f"Part 2 - Answer: {s[1]}")


if __name__ == "__main__":
    main()

########## complete ##########
