"""
Problem Description
Write a Python function that calculates the sum of all elements in a given list of integers.

Parameters:
    numbers (List of integers): The input list containing integers.
Returns:
    An integer representing the sum of all elements in the input list.

Example:
    Input: numbers = [1, 2, 3, 4, 5]
    Output: 15

    Input: numbers = [10, -5, 7, 8, -2]
    Output: 18
"""
class test_01:

    def __init__(self, value_list: list[int]):
        self.value_list = value_list

    def get_sum(self)-> int :
         total = sum(self.value_list)    
         print(total)
         return total
