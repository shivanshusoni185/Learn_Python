def arithmetic_operation(func):
    def wrapper(num1, num2):
        print("Performing arithmetic operation...")
        result = func(num1, num2)
        print("Arithmetic operation completed.")
        return result
    return wrapper

@arithmetic_operation
def add(num1, num2):
    return num1 + num2

@arithmetic_operation
def subtract(num1, num2):
    return num1 - num2

@arithmetic_operation
def multiply(num1, num2):
    return num1 * num2

@arithmetic_operation
def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2

num1 = 10
num2 = 5

result = add(num1, num2)
print(f"{num1} + {num2} = {result}")

result = subtract(num1, num2)
print(f"{num1} - {num2} = {result}")

result = multiply(num1, num2)
print(f"{num1} * {num2} = {result}")

result = divide(num1, num2)
print(f"{num1} / {num2} = {result}")
