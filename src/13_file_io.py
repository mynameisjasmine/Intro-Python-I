"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

def reader_func():
    f= open('foo.txt', 'r')
    if f.mode == 'r':
        contents = f.read()
        print(contents)
        f.close()
reader_func()


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

def writing_func():
    f=open('bar.txt', 'w+')
    for i in range(3):
        f.write("Hello, world %d\r\n" % (i+1))
    f.close()
writing_func()