# Write a Python decorator that measures the execution time of a function and logs it. Apply this decorator to a function that performs a computationally expensive task.
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result
    return wrapper

@measure_time
def expensive_computation(n):
    result = 0
    for i in range(n):
        result += sum([j ** 2 for j in range(1000)])
    return result

# Example usage:
n = 1000
print(f"Result of expensive computation: {expensive_computation(n)}")
