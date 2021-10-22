def create():
    #open a file for writing and create it if id does not exist
    f = open("guru99.txt", "w+")

    #write some lines of datea to the file
    for i in range(10):
        f.write("This is line %d\r\n" % (i+1))

    #coles the file when done
    f.close()

def write():
    f = open("guru99.txt", "a+")
    for i in range(2):
        f.write("Appended line %d\r\n" % (i+1))

def read():
    f = open("guru99.txt", "r")
    #check if the file is opened
    if f.mode == "r":
        #use f.read to read a file and store it in a variable content for reading ffiles in python
        contents = f.read()
        print(contents)

def read_in_lines():
    f = open("guru99.txt", "r")
    fl = f.readlines()
    for x in fl:
        print(x)

if __name__ == "__main__":
    #create()
    #write()
    #read()
    read_in_lines()


"""File Modes in Python
Following are the various File Modes in Python:

Mode	Description
‘r’	This is the default mode. It Opens file for reading.
‘w’	This Mode Opens file for writing.
If file does not exist, it creates a new file.
If file exists it truncates the file.
‘x’	Creates a new file. If file already exists, the operation fails.
‘a’	Open file in append mode.
If file does not exist, it creates a new file.
‘t’	This is the default mode. It opens in text mode.
‘b’	This opens in binary mode.
‘+’	This will open a file for reading and writing (updating)"""