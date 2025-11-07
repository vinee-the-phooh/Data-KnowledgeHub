# Python function template
    # Python functions are defined using the 'def' keyword.
    # The function name should be meaningful and follow the naming conventions.
    # The Function parameters should be defined in parentheses.
    # The function body should be indented.
    # The function can return a value using the 'return' statement and the return type can be specified using type hints. But type hints are optional.
    # The function can return multiple values as a tuple.
    # The function can also have default parameter values.
    # The function parameter's data type can be specified using type hints, but this is optional.
    # The function can be called by using its name followed by parentheses if no parameters are passed, or by passing the required parameters.
    # The function can also accept variable-length arguments using *args and **kwargs.

# Python functions are defined using the 'def' keyword.
def greet():
    return "Hello!"

# The function name should be meaningful and follow the naming conventions.
def calculate_area(radius: float) -> float:
    return 3.1416 * radius * radius

# The function parameters should be defined in parentheses.
def welcome(name: str):
    return f"Welcome, {name}!"

# The function body should be indented.
def is_even(n: int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False

# The function can return a value using the 'return' statement and the return type can be specified using type hints. But type hints are optional.
def square(n: int) -> int:
    return n * n

# The function can return multiple values as a tuple.
def min_max(nums: list[int]) -> tuple[int, int]:
    return min(nums), max(nums)

# The function can also have default parameter values.
def greet_user(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

# The function parameter's data type can be specified using type hints, but this is optional.
def multiply(a, b):  # No type hints
    return a * b

# The function can be called by using its name followed by parentheses if no parameters are passed, or by passing the required parameters.
def say_hello():
    return "Hi!"

# The function can also accept variable-length arguments using *args and **kwargs.
def summarize(*args: int, **kwargs: str) -> None:
    print(f"args values   : {args}")     # Tuple of positional arguments
    print(f"kwargs values : {kwargs}")   # Dictionary of keyword arguments

# Example usage of the functions
if __name__ == "__main__":
    print(greet())  # Output: Hello!
    print(calculate_area(5))  # Output: 78.54
    print(welcome("Alice"))  # Output: Welcome, Alice!
    print(is_even(4))  # Output: True
    print(square(3))  # Output: 9
    print(min_max([1, 2, 3, 4, 5]))  # Output: (1, 5)
    print(greet_user("Bob"))  # Output: Hello, Bob!
    print(multiply(2, 3))  # Output: 6
    print(say_hello())  # Output: Hi!  
    summarize(1, 2, 3, name="Alice", age="30")
    # Output:
    # args values   : (1, 2, 3)
    # kwargs values : {'name': 'Alice', 'age': '30'}