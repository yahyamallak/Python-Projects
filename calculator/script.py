import math

def menu():

    print("--------------------------------")
    print("\tOperations Menu: ")
    print("--------------------------------")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Power")
    print("6 - Root")
    print("7 - exit")

    operation = int(input("Choose operation: "))

    return operation


def addNums(a, b):
    return a + b

def subNums(a, b):
    return a - b

def multiplyNums(a, b):
    return a * b

def divideNums(a, b):
    return a / b

def power(a, b):

    result = 1

    for _ in range(b):
        result *= a 

    return result


def root(a):
    
    iteration = 3

    y = 0.5 * a

    for _ in range(iteration):
        y = 0.5 * (y + a/y)

    result = math.floor(y)

    return result


def calculator():
    
    operation = menu()

    if operation == 7:
        return operation

    number1 = int(input("Enter a number : "))

    result = 0

    if operation == 1:
        number2 = int(input("Enter second number : "))
        result = addNums(number1, number2)
    elif operation == 2:
        number2 = int(input("Enter second number : "))
        result = subNums(number1, number2)
    elif operation == 3:
        number2 = int(input("Enter second number : "))
        result = multiplyNums(number1, number2)
    elif operation == 4:
        number2 = int(input("Enter second number : "))
        result = divideNums(number1, number2)
    elif operation == 5:
        number2 = int(input("Enter second number : "))
        result = power(number1, number2)
    elif operation == 6:
        result = root(number1)

    return result



while True:

    result = calculator()

    if result == 7:
        print("Goodbye!")
        break

    print(result)


