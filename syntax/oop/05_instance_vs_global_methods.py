#Global methods are defined outside the class.
# Instance methods require 'self' and belong to objects.

def global_method():
    return "This is a global method"

class Sample:
    def instance_method(self):
        return "This is an instance method"

obj = Sample()
print(global_method())
print(obj.instance_method())

