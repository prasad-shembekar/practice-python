# Write a Python program to solve (x + y) * (x + y).

def solve(x, y):
    result = (x+y)**2
    print("({} + {}) ^ 2 = {}".format(x, y, result))


solve(4, 3)
