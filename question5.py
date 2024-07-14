# Write a Python function to compute the nth Fibonacci number using recursion.

def fibonacci(n):
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
n = int(input("Enter the number: "))
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
