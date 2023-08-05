# Write a Python program to get the execution time of a Python method.

import time


def prog_time(n):
    start = time.time()
    s = 0
    for i in range(1, n+1):
        s = s + i
    end = time.time()
    return s, end-start


n = 5
print("Time taken:", prog_time(n))
