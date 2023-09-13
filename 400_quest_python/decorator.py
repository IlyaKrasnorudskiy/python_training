import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time} seconds")
        return result
    return wrapper

@timer_decorator
def example_function(duration):
    time.sleep(duration)
    print(f"Slept for {duration} seconds")

example_function(2)
