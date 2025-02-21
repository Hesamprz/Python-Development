import math

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2

def sqrt(num):
    if num < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return math.sqrt(num)

def sin(angle):
    return math.sin(math.radians(angle))

def cos(angle):
    return math.cos(math.radians(angle))

def tan(angle):
    return math.tan(math.radians(angle))

def cot(angle):
    if angle % 180 == 0:
        raise ValueError("Cotangent is undefined for this angle")
    return 1 / math.tan(math.radians(angle))
