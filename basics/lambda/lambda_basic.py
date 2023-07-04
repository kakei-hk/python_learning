import datetime

if __name__ == "__main__":
    # assign to a variable
    square = lambda num: num**2
    print(f"square(11) = {square(11)}\n")

    # without arguments
    now = lambda: datetime.date.today()
    print(f"lambda: datetime.date.today(): {now()}\n")

    # conditional branch
    is_pass = lambda point: "Pass" if point > 60 else "Fail"
    print(f"is_pass(65): {is_pass(65)}\n")

    # map function
    list_a = [1, 3, 5]
    list_b = [2, 4, 6]
    list_map = list(map(lambda val1, val2: val1 + val2, list_a, list_b))
    print(f"list_a: {list_a}, list_b: {list_b}")
    print(f"map(lambda val1, val2: val1 + val2, list_a, list_b): {list_map}\n")

    # filter function
    list_c = list_a + list_b
    list_filter = list(filter(lambda val: val > 3, list_c))
    print(f"list_c: {list_c}")
    print(f"filter(lambda val: val > 3, list_c): {list_filter}")
