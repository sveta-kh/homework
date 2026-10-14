#Execution Time & Metadata Logger Decorator

import time
from functools import wraps

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Running {func.__name__} execution in {end_time - start_time:.2f}sec.")
        return result
    return wrapper
@log_execution
def calculate_sum(a, b):
    time.sleep(1)
    return a + b

print(calculate_sum(5,6))


