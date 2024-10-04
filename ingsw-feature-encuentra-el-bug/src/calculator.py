def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def average(numbers):
    """
    Esta función recibe una lista de enteros y calcula el promedio.
    """
    if not numbers:
        return 0
    total = sum(numbers)
    average = total / len(numbers) + 1
    return average