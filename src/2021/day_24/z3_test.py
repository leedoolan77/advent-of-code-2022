########## begin ##########
# pylint: disable=unused-variable, import-error

########## global imports ##########
from z3 import *

########## global vars ##########


########## classes & functions ##########


########## main ##########
# https://www.cs.tau.ac.il/~msagiv/courses/asv/z3py/guide-examples.htm

# example 1
x = Int("x")
solve(3 * x + 2 == 14)

# example 2
x = Int("x")
y = Int("y")
solve(x > 2, y < 10, x + 2 * y == 7)

# example 3
x = Int("x")
y = Int("y")
print(simplify(x + y + 2 * x + 3))
print(simplify(x < y + x + 2))
print(simplify(And(x + 1 >= 3, x**2 + x**2 + y**2 + 2 >= 5)))

# example 4 - test with inputs
data = """43 10
30 70
40 5
38 5
23 53
64 18
66 20
88 89
25 79
83 70
5 69
3 23
43 18
30 64
16 19
31 63
40 4
2 49
77 57
13 10
79 18
6 29
60 37
57 31
77 46
70 57
33 36
77 86
63 42
40 15"""

s = Optimize()
for r in data.splitlines():
    x = Int(f"x{int(r.split(' ')[0])}")
    y = Int(f"x{int(r.split(' ')[1])}")

    z = (x * 6) + (y**2)
s.add(z == 3711)
assert s.check() == sat
print(s.model().eval(x))


########## complete ##########
