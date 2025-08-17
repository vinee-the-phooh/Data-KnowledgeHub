
# Python Imports — Using modules and functions

# What is an import?

    # In Python, we can use code from other files or built-in libraries by importing them.
    # This helps we reuse functions, classes, and tools without rewriting them.
    # - Use `import module` to access everything with module name
    # - Use `from module import item` to access specific parts directly
    # - Use aliases with `as` to shorten names

#1. Basic import
# This imports the entire module
import math

#We now access functions using the module name
print(math.sqrt(16))  # Output: 4.0
print(math.pi)        # Output: 3.141592653589793

#2. from ... import
# This imports specific functions or variables directly
from math import sqrt, pi

# You can now use them without the module name
print(sqrt(25))  # Output: 5.0
print(pi)        # Output: 3.141592653589793

#3. Import with alias (like a nickname)
# Useful for shortening long module names
import numpy as np
# Now we can use np instead of numpy
# Example: np.array([...]) 

# 4. from ... import with alias
from math import sqrt as square_root
print(square_root(36))  # Output: 6.0

# 5. Importing custom modules
# If we have a file called `my_utils.py` with a function `greet()`,
# we can import it like this:
# import my_utils
# my_utils.greet()

# Or:
# from my_utils import greet
# greet()

