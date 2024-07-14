# Write a Python function that divides two numbers and handles the case where the divisor is zero by returning a custom error message.

def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# Example usage:
num = 10
den = 0
print(f"Division result: {safe_divide(num, den)}")

den = 2
print(f"Division result: {safe_divide(num, den)}")
