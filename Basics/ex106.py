# Write a Python program to divide a path by the extension separator.

import os.path
for path in ['test.txt', 'filename', '/user/system/test.txt', '/', '']:
    print('"%s" :' % path, os.path.splitext(path))
