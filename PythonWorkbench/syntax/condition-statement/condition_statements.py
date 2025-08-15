#Python Conditional Statements

    # - Use 'if' to check conditions and control flow
    # - Use 'elif' for multiple checks, and 'else' for fallback
    # - Indentation is required — no curly braces
    # - Logical operators: and, or, not
    # - Use 'in' for membership, 'is' for identity
    # - Conditions can be nested or written in shorthand
    # - Python is case-sensitive when comparing strings
    # - Avoid using '=' (assignment) inside conditions — use '==' for comparison



#1. Basic 'if' Statement
# Executes the block only if the condition is True
# Note: No parentheses or curly braces needed (unlike Java)
# Indentation is required to define the block
x = 10
if x > 5:
    print("x is greater than 5")

#2. 'if-else' Statement
# Provides an alternative block if the condition is False
age = 17
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

#3. 'if-elif-else' Chain
# Checks multiple conditions in order
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

#4. Nested Conditions
# Conditions inside other conditions
user = {"name": "Lili", "active": True, "role": "admin"}
if user["active"]:
    if user["role"] == "admin":
        print("Access granted")
    else:
        print("Limited access")
else:
    print("User is inactive")

#5. Shorthand 'if' (single-line)
x = 5
if x == 5: print("x is 5")  # One-liner if statement

#6. Shorthand 'if-else' (ternary operator)
y = 10
result = "even" if y % 2 == 0 else "odd"
print(result)  # even

#7. Logical Operators: and, or, not
a = 7
b = 12
if a > 5 and b > 10:
    print("Both conditions are true")

if a < 5 or b > 10:
    print("At least one condition is true")

if not a == 5:
    print("a is not equal to 5")

#8. Comparing Values
# ==, !=, >, <, >=, <=
temp = 36.5
if temp == 36.5:
    print("Normal temperature")

if temp != 37:
    print("Not a fever")

#9. Comparing Strings
name = "Lily"
if name == "Lily":
    print("Welcome Lily")

# Note: String comparison is case-sensitive
if name == "lily":
    print("Lowercase match")  # Won't print

#10. Checking Membership with 'in'
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is available")

#11. Boolean Conditions
is_logged_in = True
if is_logged_in:
    print("User is logged in")

#12. Using 'is' for Identity Comparison
x = None
if x is None:
    print("x is None")

#13. Using Conditions in Functions
def check_even(n: int) -> str:
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even(4))  # Even

#14. Using Conditions in Loops
for num in range(5):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

#15. Equality: x == 5
x = 5
if x == 5:
    print("x is 5")  #True — value matches

#16. Inequality: x != 5
x = 3
if x != 5:
    print("x is not 5")  #True — value does not match

#17. Negation with 'not': not x == 5
x = 3
if not x == 5:
    print("x is not 5 (using 'not')")  #Same as x != 5

#18. String Equality: name == "Lili"
name = "Lili"
if name == "Lili":
    print("Hello Lili")  #True — exact match

#19. String Inequality: name != "Lili"
name = "Mark"
if name != "Lili":
    print("Not Lili")  #True — different name

#20. Negation with 'not': not name == "Lili"
name = "Mark"
if not name == "Lili":
    print("Name is not Lili (using 'not')")  #Same as name != "Lili"


#21. Using 'not' and '==':
if not name == "Lili":
    print("Uing 'not' and '=='")