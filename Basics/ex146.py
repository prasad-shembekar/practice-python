# Write a Python program to find the location of Python module sources.

import imp 
print("Location of python os module")
print(imp.find_module('os'))
