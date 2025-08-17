
#Python Exception Handling
    # - Use try-except to catch errors and prevent crashes
    # - Use else for code that runs only if no error occurs
    # - Use finally for cleanup (runs no matter what)
    # - Catch specific exceptions for clarity
    # - Avoid using bare 'except:' — it hides bugs
    # - Use custom exceptions to describe domain-specific errors
    # - Use assert for quick checks during development
    # - Use 'raise' to trigger exceptions manually
# Best practice: use specific exceptions
    # Avoid catching all exceptions if NOT necessary
    # Always log or re-raise if it is needed


#1. Basic try-except
# Use try-except to catch raised exceptions and prevent program crashes
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# 2. Catching multiple exceptions
# We can catch different types of errors separately
try:
    value = int("abc")
    result = 10 / 0
except ValueError:
    print("Invalid conversion to int")
except ZeroDivisionError:
    print("Division by zero error")

#3. Catching multiple exceptions in one block

try:
    x = int("abc")
except (ValueError, TypeError):
    print("Caught ValueError or TypeError")

# 4. Using else with try
# The else block runs only if no exception occurs
try:
    num = int("42")
except ValueError:
    print("Conversion failed")
else:
    print(f"Conversion succeeded: {num}")

# 5. Using finally
# The finally block always runs — useful for cleanup
try:
    f = open("sample.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing file (if open)")
   

#6. Catching all exceptions (But NOT recommended)
try:
    risky = 1 / 0
except Exception as e:
    print(f"Something went wrong: {e}")

#7.Custom exception class
# We can create our own error types to describe specific problems in our modules
# This helps us to understand what went wrong and handle different errors separately
class NegativeNumberError(Exception):
    """Raised when a negative number is not allowed."""
    pass

def check_positive(n: int):
    if n < 0:
        raise NegativeNumberError("Negative value not allowed")
    return n

try:
    check_positive(-5)
except NegativeNumberError as e:
    print(f"Custom error: {e}")

#8.Raising exceptions manually and trigger an error intentionally
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

try:
    divide(10, 0)
except ZeroDivisionError as e:
    print(f"Manual raise: {e}")


