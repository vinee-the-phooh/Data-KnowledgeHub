# This function uses 'yield' to return one even number at a time.
# It does not store all numbers in memory, it creates them as needed.

def even_numbers(limit):
    num = 0  # Start from 0
    while num <= limit:  # Keep going until we reach the limit
        if num % 2 == 0:  # Check if the number is even
            yield num     #'yield' sends the number out to the for loop (even_number method), where it gets printed. Then it pauses the function and waits to continue from the same spot.
        num += 1          # Move to the next number

#Using the generator
    # This loop calls the generator and prints each even number it produces.
    # The generator remembers where it stopped and continues from there.

for even in even_numbers(10):
    print(even)  # Output: 0, 2, 4, 6, 8, 10