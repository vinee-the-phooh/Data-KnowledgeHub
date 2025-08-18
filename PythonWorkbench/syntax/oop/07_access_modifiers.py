# Access Modifiers in Python
# Access modifiers in Python are used to define the visibility and accessibility of class attributes and methods.
# Python has three main access modifiers:
# Public: Accessible from anywhere.
# Protected: Intended for internal use within the class and its subclasses.
# Private: Intended for internal use within the class only, using name mangling.
# Access modifiers in Python are not enforced like in some other languages like Java, but they are a convention to indicate the intended use of class attributes and methods. 
    #Public: no underscore (accessible everywhere).
    #Protected: one underscore (_) — hint to avoid direct access.
    #Private: two underscores (__) — name mangling hides it.

class AccessDemo:
    def __init__(self):
        self.public_var = "Public"
        self._protected_var = "Protected"
        self.__private_var = "Private"

    def show(self):
        print(self.public_var)
        print(self._protected_var)
        print(self.__private_var)

obj = AccessDemo()
obj.show()

