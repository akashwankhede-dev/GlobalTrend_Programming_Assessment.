# Write a Python function that takes two numbers and an operator (as a string) and performs the corresponding arithmetic operation (addition, subtraction, multiplication, or division).

def arithmetic_operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator. Please use one of '+', '-', '*', '/'."

# Example usage:
num1 = 10
num2 = 5

print(f"{num1} + {num2} = {arithmetic_operation(num1, num2, '+')}")
print(f"{num1} - {num2} = {arithmetic_operation(num1, num2, '-')}")
print(f"{num1} * {num2} = {arithmetic_operation(num1, num2, '*')}")
print(f"{num1} / {num2} = {arithmetic_operation(num1, num2, '/')}")
print(f"{num1} / 0 = {arithmetic_operation(num1, 0, '/')}")
print(f"{num1} % {num2} = {arithmetic_operation(num1, num2, '%')}")
