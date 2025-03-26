# Timing Decorator:
 #       1. Write a decorator @timing that measures the time it takes for a function to execute and prints the execution time. Apply this decorator to various functions and compare their execution times
import time
import functools

def timing(func):
    """Decorator to measure the execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Start the timer
        result = func(*args, **kwargs)
        end_time = time.perf_counter()    # End the timer
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds.")
        return result
    return wrapper
# 1) Function with a sleep delay
# The function simulates a delay using  time.sleep()
@timing
def sleep_function():
#"This function sleeps for 2 sec"
     time.sleep(2)
     return "Finished sleeping"
sleep_function()
#computational task
@timing
def compute_squares(n):
    """Function that computes the sum of squares up to n."""
    return sum(i * i for i in range(n))
compute_squares(10**6)
#String Manipulation
@timing
def concatenate_strings(n):
    result=''
    for i in range(n):
         result += 'S'
    return result
concatenate_strings(10**5)   
#For more advanced forms timed-decorator (external libraries) can be used.
from timeit_decorator import timeit

@timeit(runs=5, workers=2)
def sample_function():
    pass
sample_function()
