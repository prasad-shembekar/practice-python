# Write a Python program to make file lists from the current directory using a wildcard. 

import glob 
file = glob.glob('*.*')
print(file)
print(glob.glob('.py'))
