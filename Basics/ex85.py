# Write a Python program to check whether a file path is a file or a directory.

import os
path = "ex30.py"

if os.path.isdir(path):
    print("It is a directory")
elif os.path.isfile(path):  
    print("\nIt is a normal file")  
else:  
    print("It is a special file (socket, FIFO, device file)" )
print()