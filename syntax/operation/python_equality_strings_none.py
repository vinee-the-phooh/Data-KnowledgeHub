#Python Equality, Strings, and None
    # - Use '==' for value comparison
    # - Use 'is' for identity comparison (especially with None)
    # - Both "" and '' are valid string delimiters
    # - None represents "no value" and is not equal to ""
    # - Empty strings, None, 0, and empty containers are falsy
    # - Use 'if not value:' to check for falsy values


#1. Equality with '=='
# '==' checks if two values are equal (not identity)
a = "hello"
b = "hello"
print(a == b)  #Output : True — both strings have the same value

#2. Identity with 'is'
# 'is' checks if two variables point to the same object in memory
print(a is b)  #utput : True — string interning makes them share memory

# For larger objects like lists, '==' compares content, 'is' compares identity
list1 = [1, 2]
list2 = [1, 2]
print(list1 == list2)  #Output :  True — same content
print(list1 is list2)  #Output : False — different memory locations

#3. Strings: "" vs ''
# Both double and single quotes are valid for strings
s1 = "Python"
s2 = 'Python'
print(s1 == s2)  #Output : True


# 4. None — Python's null-like object
name = None  # name Represents absence of value
# Check for None using 'is'
# Avoid using '==' to compare with None — 'is' is preferred
if name is None:
    print("name is None")



#5. Empty String vs None
# Important: "" and None are NOT the same
empty_str = ""
none_value = None

print(empty_str == "")     #Output :   True — it is an empty string
print(none_value is None)  #Output :   True — it is a None object


# 6. Truthy and Falsy Values
    # These values are considered False in conditions:
    # - None
    # - False
    # - 0
    # - ""
    # - []
    # - {}

if not "":
    print("Empty string is falsy")

if not None:
    print("None is falsy")

if not 0:
    print("Zero is falsy")

if not []:
    print("Empty list is falsy")

