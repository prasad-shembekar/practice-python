# Write a Python program to get the length in bytes of one array item in the internal representation

from array import *

array_num = array('i',[1,3,5,7,9])
print("length in bytes:"+str(array_num.itemsize))