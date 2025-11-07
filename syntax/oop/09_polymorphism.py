#Polymorphism in Python
# Polymorphism is a core concept in object-oriented programming.
# It allows objects of different classes to be treated as objects of a common superclass.
# It enables methods to do different things based on the object they are called on,
# even if they share the same method name.

class Bird:
    def sound(self):
        return "Generic bird sound"

class Parrot(Bird):
    def sound(self):
        return "Squawk!"

class Crow(Bird):
    def sound(self):
        return "Caw!"

birds = [Parrot(), Crow()]
for bird in birds:
    print(bird.sound())

# Output:
# Squawk!
# Caw!
# In this example, both Parrot and Crow classes inherit from the Bird class.
# They override the sound method to provide their specific implementations.
# When we call the sound method on each object in the birds list,Python dynamically determines which method to execute based on the actual object type,