# self_explained.py
# This module shows why we use 'self' in class methods, even if we don't use any variables.

# What is 'self'?
    # 'self' is a reference to the current object.
    # It is automatically passed when we call a method using an object.
    # It lets the method know which object is calling it.


# Example : Simple class with one method

class Hello:
    # 'self' is required in all instance methods
    # Even though we don't use any variables here,
    # Python still passes the object when we call this method.
    def say_hello(self):  
        print("Hello there!")


# Create an object of the Hello class
obj_hello = Hello()

# Call the method using the object
# Python automatically passes 'obj_hello' as the first argument to say_hello()
obj_hello.say_hello()