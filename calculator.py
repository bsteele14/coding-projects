# Simple Arithmetic Calculator
# that calculates the result of two numbers (num1 & num2)
# given a specific operand(+,-,/,*)

# Defining the Functions of the Operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

# Display a menu to the user

print("Select The Operation")
print("--------------------")
print("(1) ADD")
print("(2) SUBTRACT")
print("(3) MULTIPLY")
print("(4) DIVIDE")

#Ask for selection
op = input("Enter Operation(1,2,3,or 4): ")

#Ask user to input numbers to be used in the operation
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if op == '1':
    print(num1," + ",num2," = ", add(num1, num2))

elif op == '2':
    print(num1," - ",num2," = ", subtract(num1, num2))

elif op == '3':
    print(num1," * ",num2," = ", mult(num1, num2))

elif op == '4':
    print(num1," / ",num2," = ", div(num1, num2))

else:
    print("Invalid Input")

print("Thank You For Using The Calculator")

