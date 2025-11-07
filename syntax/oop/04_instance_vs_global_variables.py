# - Global variables are defined outside the class.
# - Instance variables use 'self' and are unique to each object.

global_var = "I am global"  # Global variable

class Demo:
    def __init__(self, value):
        self.instance_var = value  # Instance variable

    def show(self):
        print("Instance:", self.instance_var)
        print("Global:", global_var)

demo = Demo("I am instance")
demo.show()


