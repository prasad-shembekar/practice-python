# Write a Python program to determine the profiling of Python programs.

import cProfile


def sum():
    print(1+2)


cProfile.run('sum()')
