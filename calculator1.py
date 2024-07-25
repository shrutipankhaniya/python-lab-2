# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def percentage(total, part):
    if total == 0:
        raise ValueError("Total cannot be zero for percentage calculation")
    return (part / total) * 100
