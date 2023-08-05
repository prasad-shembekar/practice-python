# Write a Python program that retrieves the date and time of file creation and modification.

import os.path
import time
print("Last modified: %s" % time.ctime(os.path.getmtime("ex60.py")))
print("Created: %s" % time.ctime(os.path.getctime("ex60.py")))
