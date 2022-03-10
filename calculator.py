import math
# Defining the math functions

def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def modulus(num1, num2):
    return num1 / num2
def sin(num1):
    return math.sin(math.radians(num1))
def cos(num1):
    return math.cos(math.radians(num1))
def tan(num1):
    return math.tan(math.radians(num1))
def cot(num1):
    return (1 / math.tan(math.radians(num1)))

# Defining the switch function

def switch(operation, num1, num2):

    dict={
        1: addition(num1, num2),
        2: subtraction(num1, num2),
        3: multiply(num1, num2),
        4: modulus(num1, num2)
    }
    return dict.get(operation, 'Invalid Operation')

# Defining the switch2 function

def switch2(operation, num1):

    dict={
        5: sin(num1),
        6: cos(num1),
        7: tan(num1),
        8: cot(num1),
    }
    return dict.get(operation, 'Invalid Operation')

# Taking user input to choose an operation

print('''
Press 1 for Addition
Press 2 for Subtraction
Press 3 for Multiplication
Press 4 for finding the remainder after division
Press 5 for sin
Press 6 for cos
Press 7 for tan
Press 8 for cot
''')
num = int(input('Enter a number of your choice: '))

if num < 5 :

    # Taking the operands from the users
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))

    # Calling the switch function
    print('Result is: ', switch(num, num1, num2))


else :
    # Taking the operand from the users
    num1= int(input('Enter the number: '))

    # Calling the switch2 function
    print('Result is: ', switch2(num, num1))

