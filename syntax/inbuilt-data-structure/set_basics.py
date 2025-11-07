#This module explains Python sets

#What is a set? 
    # A set is a collection of unique items. No duplicates allowed.
    # Sets are unordered — items have no fixed position.
    # No indexing (we can't do set[0])
    # Sets use a data structure called a hash table,which makes checking whether an item is available or not much faster than other data structures, especially when the set contains many items.       

#Creating a set
numbers = {1, 2, 3, 4, 4, 2}
print(numbers)  # {1, 2, 3, 4} — duplicates removed

#Adding items
numbers.add(5)

#Removing items
numbers.remove(2)     # Removes 2
numbers.discard(10)   # Safe remove (no error if not found)

#Looping through a set
for num in numbers:
    print(num)

