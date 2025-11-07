#Comparing generator and list for memory usage
    #Generator is better for large data — uses less memory

# List stores all values in memory
list_nums = [x * x for x in range(1000000)]

# Generator creates values one by one (lazy evaluation)
gen_nums = (x * x for x in range(1000000))

#We can loop through both
for num in gen_nums:
    if num > 100:
        break
    print(num)

