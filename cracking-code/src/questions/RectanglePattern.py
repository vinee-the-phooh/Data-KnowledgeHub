"""
Problem Description:
You are given two integers, n and m. Your task is to return a rectangle pattern of '*', 
where n represents the number of rows (length) and m represents the number of columns (breadth).

Input:
    Two integers n and m, where 1 <= n, m <= 100.


Output:
    A list of strings where each string represents a row of the rectangle pattern.

Example:
    Input: n = 4, m = 5
    Output: ['*****', '*****', '*****', '*****']
     
    Input: n = 3, m = 2
    Output: ['**', '**', '**']

"""

class Pattern_03:

    def __init__(self, number, column):
        self. number = number
        self.column = column
    
    def print_pattern(self):
        list_pattern =[]
        if self.column >=1 and self.number <= 100:
            for _ in range(self.column):
                raw_str = "*"*self.number
                list_pattern.append(raw_str)
        print(list_pattern)
