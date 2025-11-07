#Python Loop Module - while loop
    # - Use while loops when the number of repetitions is unknown (as Java does).
    # - The loop runs as long as the condition is True
    # - Use break to exit early, continue to skip one iteration
    # - Use else to run code after normal loop completion
    # - Be mindful with infinite loops — always update the condition
    # - Great for waiting for changes (as long as the condition is True)


# What is a while loop?
# A while loop repeats a block of code as long as (NOT Until) a condition is True.
# It checks the condition before each iteration.

#1. Basic while loop
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

# Output:
# Count is: 0
# Count is: 1
# Count is: 2

#2. Using break to exit early
x = 0
while x < 10:
    print(x)
    if x == 5:
        break
    x += 1

# Output:
# 0 to 5, then stops

#3. Using continue to skip an iteration
y = 0
while y < 5:
    y += 1
    if y == 3:
        continue
    print("y =", y)

# Output:
# y = 1
# y = 2
# y = 4
# y = 5

#4. Using else with while loop
# The else block runs only if the loop ends normally (not by break)
z = 0
while z < 3:
    print("z =", z)
    z += 1
else:
    print("Loop ended without break")


