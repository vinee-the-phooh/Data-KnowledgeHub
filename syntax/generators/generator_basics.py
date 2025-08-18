#What is a generator?
    # A generator is a special type of function that returns an iterator.
    # It uses the 'yield' keyword instead of 'return'.
    # Each time the generator is called, it resumes from where it left.

def simple_generator():
    yield 1
    yield 2
    yield 3

#How to use the generator
gen = simple_generator()

#Each call to 'next()' gives the next value
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
# print(next(gen))  #Raises StopIteration (no more items)