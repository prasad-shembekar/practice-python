# Write a Python program to get the name of the host on which the routine is running.

import os
import platform
import socket
host_name = socket.gethostname()
print("Host name:", host_name)

host_name = platform.uname()[1]
print("Host name:", host_name)

print("Host name:", host_name)
