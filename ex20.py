#initial command for arguments
from sys import argv

script, input_file = argv

# First function that reads the argument.
def print_all(f):
    print(f.read())

# Second function which "rewinds" the past function to 0.
def rewind(f):
    f.seek(0)

# Third function with 2 arguments, the secon argument has the command to only read 1 line of the .txt.
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Variable that opens our file that will be used for the functions (.txt.)
current_file = open(input_file)

# Introductory "print"
print("First let's print the whole file: \n")
# Displays FIRST function, which has only 1 argument.
print_all(current_file)

# Introductory "print"
print("\nNow let's rewind, kind of like a tape.")
# Dispalys SECOND function, which rewinds the file chosen (current_file).
rewind(current_file)

# Introductory "print"
print("\nLet's print three lines: ")
# Displays THIRD function, creates a variable that has a number.
current_line = 1
print_a_line(current_line, current_file)
 
 # The variable created gets changed on this line, the comman .readline helps the function to not take count of the others, and if it did it will have a + 1.
current_line = current_line + 1
print_a_line(current_line, current_file)

# The variable changed gets changed again, with a + 1 besides the + 1 before it. Displays just the third line of the function.
current_line = current_line + 1
print_a_line(current_line, current_file)