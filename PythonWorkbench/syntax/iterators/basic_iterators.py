#This module explains what iterators are and how they work with built-in Python objects.

#What is an iterator?
    # An iterator is an object that lets us go through items one by one.
    # We can use it in loops like for, or manually with next().


#Example 1: Using a for loop (automatic iterator)
fruits = ["apple", "banana", "cherry"]
# Python automatically uses an iterator behind the operations
for fruit in fruits:
    print(fruit)


#Example 2: Manual iteration using iter() and next()    
    # 'iter()' creates an iterator from a sequence
    # 'next()' gets the next item from the iterator

numbers = [10, 20, 30]
num_iter = iter(numbers)  # Create an iterator

print(next(num_iter))  # 10
print(next(num_iter))  # 20
print(next(num_iter))  # 30
# print(next(num_iter))  #Raises StopIteration if no items left
