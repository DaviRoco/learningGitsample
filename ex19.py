def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Get a blanket. \n")

print("We can just give the function numbers directly: ")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script: ")
amount_cheese = 10
amount_crackers = 50

cheese_and_crackers(amount_cheese, amount_crackers)

print("We can even do math inside too: ")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and numbers: ")
cheese_and_crackers(amount_cheese + 100, amount_crackers + 1000)