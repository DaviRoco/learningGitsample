def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBSTRACTION {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"dividing {a} / {b}")
    return a / b

print("Let's do math with these functions. ")

age = add(14, 555)
height = subtract(978, 74)
weight = multiply(180, 2)
iq = divide(180, 2)

print(f"\n Age: {age},\n Height: {height},\n Weight: {weight},\n IQ: {iq}")

print("\n Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes:", what, "Can you do it by hand? ")