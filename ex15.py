#Imports argument variables from system, this means we can import any ex.py and display it.
from sys import x

# We give the variables to the argument variables
script, filename = x

# We create a variable to open a variable (in this case ex15_sample.txt.)
txt = open(filename)

# Prints our variable at line 11 as a string, but reads it at line 12 because we command it to read txt (variable of open(filename))
print(f"Here's your file {filename}:")
print(txt.read())
#print(txt.close())

#Prints the question of the input.
#print("Type the filename again:")
#Writes the input with the variable name: file_again
#file_again = input("> ")

#We create another variable to open our input.
#txt_again = open(file_again)

#We print the variable txt_again and we command it to read ex15_sample.txt. or any other file and display it.
#print(txt_again.read())
#print(txt_again.close())