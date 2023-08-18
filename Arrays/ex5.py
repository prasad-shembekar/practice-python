from array import *
array_num = array('i',[1,3,5,7,9])
print("Buffer info:"+str(array_num.buffer_info()))
print("Buffer bytes:"+str(array_num.buffer_info()[1]*array_num.itemsize))