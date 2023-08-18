# Write a Python program to convert an array to an ordinary list with the same items.

from array import *

array_num = array('i',[1,3,5,3,7,1,9,3])
num_list = array_num.tolist()
print(num_list)