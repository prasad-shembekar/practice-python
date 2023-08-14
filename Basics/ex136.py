# Write a Python program to find files and skip directories in a given directory.

import os
print([f for f in os.listdir('/home/students') if os.path.isfile(os.path.join('/home/stduents',f))])