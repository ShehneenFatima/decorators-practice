#Decorators
#Parameterised Decorator:
# 1. Create a decorator @repeat(n) that repeats the decorated function n times. It should also accept an argument for whether to print the results each time. Apply this decorator to a simple function.
import functools

def repeat(n, print_results=True):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                result = func(*args, **kwargs)
                results.append(result)
                if print_results:
                    print(result)
            return results
        return wrapper
    return decorator

@repeat(3, print_results=True)
def greet(name):
    return f"Happy Birthday, {name}!"

greet("Shehneen Fatima")


