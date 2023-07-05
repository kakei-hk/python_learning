import random
from functools import lru_cache


# decorator
def log_function(function):
    # define inner function
    def wrapper(*args, **kwargs):
        print("--------------------")
        print(f"function name: {function.__name__}")
        print(f"arguments: {args}")
        print(f"keyword arguments: {kwargs}")
        print("--------------------")
        # execute original function
        return function(*args, **kwargs)

    return wrapper


@log_function
def print_coordinate(x, y, z=0, type="cartesian"):
    print(f"({x}, {y}, {z}) ({type})")


# use lru_cache decorator
@lru_cache(maxsize=4)
def get_rand_int(min=0, max=100):
    return random.randint(min, max)


if __name__ == "__main__":
    print_coordinate(2.0, 3.8, -6.7)
    print()

    print(f"get random value #1: {get_rand_int()}")
    print(f"get random value #2: {get_rand_int()}")
