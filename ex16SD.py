# This is going to ask the user to login.
from sys import argv

script, database = argv

print("Hello user, we are going to ask you some questions.")
input("Continue? ")
target = open(database, 'w')
print("OK.")


print("Preparing the scene")

q1 = input("First question: What is your name? ")
q2 = input("Second question: Which is your favorite color? ")
q3 = input("Third question: Which is your favorite videogame? ")

target.write(f" The user is {q1}, its favorite color is {q2}, its favorite game is {q3}")

target_2 = open(database, 'r')
print(f"Excellent!. Now let's make sure we got right you file: {database} ")
print(target_2.read()) 