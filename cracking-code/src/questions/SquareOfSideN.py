"""
    Problem Description: You are given an integer n. 
    Your task is to return a square pattern of size n x n made up of the character '*', 
    represented as a list of strings.

Input Parameters:
    n (int): The size of the square (number of rows and columns).

Output:
    A list of strings where each string is a row of n characters.

Example:

    Input: 3
    Output: ['***', '***', '***']
     
    Input: 5
    Output: ['*****', '*****', '*****', '*****', '*****']
"""

class Pattern_01:   
     def __init__(self,number: int):
          self.number = number 
        
     def print_pattern(self):
         pattern_list  = []
         for _ in range(self.number):
              raw_str = "*" * self.number
              pattern_list.append(raw_str)
         print(pattern_list)
                    
                     

     