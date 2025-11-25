"""
Problem Description:
You are given an integer n. 
Your task is to return a hollow square pattern of size n x n made up of the character '*', represented as a list of strings. 
The hollow square has '*' on the border, and spaces ' ' in the middle (except for side lengths of 1 and 2).

Input Parameters:
    n (int): The size of the square (number of rows and columns).

Output:
    A list of strings where each string is a row of n characters, representing a hollow square.

Example:
    Input: 3
    Output: ['***', '* *', '***']
    Input: 5
    Output: ['*****', '*   *', '*   *', '*   *', '*****']
"""

class Pattern_02:

    def __init__(self,number):
        self.number = number

    def print_pattern(self):
        pattern_list = []
        value = self.number
        while(value>0):
            if value == self.number or value == 1:
                raw_str = "*"*self.number
                pattern_list.append(raw_str)
                
            else:
                raw_str = " "*(self.number-2)
                raw_str = "*"+raw_str+"*"
                pattern_list.append(raw_str)
                
            value = value -1 
        print(pattern_list)