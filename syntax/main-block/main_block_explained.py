# Python __main__ Block — What It Means and Why It Matters
# What is __name__?
    # Every Python file has a built-in variable called __name__
    # Python sets this value depending on how the file is used:
        # - If the file is run directly : __name__ == "__main__"
        # - If the file is imported into another file : __name__ == "filename"

# Why use `if __name__ == "__main__"`?
    # This condition lets us control what code runs when:
        # Run the file directly :  the block runs
        # Import a file with a if __name__ == "__main__" block into another file :  the block is skipped
        # This helps us to write reusable code that doesn't run automatically when imported

# Example: Define a reusable function
def greet(name):
    print(f"Hello, {name}!")

# Call the function only when this file is executed directly
if __name__ == "__main__":
    greet("Harsha")  # Output: Hello, Harsha!