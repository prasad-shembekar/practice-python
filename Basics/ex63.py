# Write a Python program to get an absolute file path.

def absolute_path(path):
    import os
    return os.path.abspath('path_fname')


print(absolute_path("ex60.py"))
