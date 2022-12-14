########## begin ##########
# pylint: disable=unused-variable, import-error

########## global imports ##########
from mylib.general import read_file_into_var, get_file_path

########## global vars ##########
testing = False

########## classes & functions ##########
def get_input_file_data(testing):
    input_file = (
        f"{get_file_path(__file__)}/{'input_example.txt' if testing else 'input.txt'}"
    )
    return read_file_into_var(input_file)


def make_list(x):
    return x if type(x) is list else [x]


def compare(l, r):
    # test integers
    if type(l) is int and type(r) is int:
        if l < r:
            return True
        elif l > r:
            return False
        else:
            return None

    # else make both lists, loop thru with recursion
    l, r = make_list(l), make_list(r)
    for x, y in zip(l, r):
        res = compare(x, y)
        if res is None:
            continue
        else:
            return res

    # now test lengths
    if len(l) == len(r):
        return None
    return True if len(l) < len(r) else False


def sort(a):  # bubble sort, reuse compare method
    n = len(a)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if not compare(a[j], a[j + 1]):  # compare here
                swapped = True
                a[j], a[j + 1] = a[j + 1], a[j]
        if not swapped:
            return


def solve(input_file_data):
    packets = [
        (eval(p.split("\n")[0]), eval(p.split("\n")[1]))
        for p in input_file_data.split("\n\n")
    ]

    part_one = sum([n + 1 for n, p in enumerate(packets) if compare(*p)])

    # part two
    all_packets = (
        [eval(p) for p in input_file_data.splitlines() if p] + [[[2]]] + [[[6]]]
    )
    sort(all_packets)
    part_two = 1
    for x in [n + 1 for n, p in enumerate(all_packets) if p in [[[2]], [[6]]]]:
        part_two *= x

    return (part_one, part_two)


########## main ##########
def main():
    s = solve(get_input_file_data(testing))

    print(f"Part 1 - Answer: {s[0]}")
    print(f"Part 2 - Answer: {s[1]}")


if __name__ == "__main__":
    main()

########## complete ##########
