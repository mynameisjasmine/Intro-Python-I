"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print('Argument 1', str(sys.argv[0]))
print('Argument 2', str(sys.argv[1:]))

for i in sys.argv:
    print('new sys.arg', i)

import platform
# Print out the OS platform you're using:
print('Platform:', platform.system())
print('New Platform:',sys.platform)

# Print out the version of Python you're using:
print('Python Version:', sys.version)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print('Process ID:', os.getpid())

# Print the current working directory (cwd):
print('Current Working Directory:', os.getcwd())

import getpass
# Print out your machine's login name
print('Login Name:', getpass.getuser())

