#Imports argument variables from system, this means we can import any ex.py and display it.
from sys import argv

# We give the variables to the argument variables
script, filename = argv

# We create a variable to open a variable (in this case ex15_sample.txt.)
txt = open(filename)

#We create another variable to open our input.
txt_again = open(file_again)

#We print the variable txt_again and we command it to read ex15_sample.txt. or any other file and display it.
print(txt_again.read())