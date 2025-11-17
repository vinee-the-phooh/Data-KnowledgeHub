"""
Problem Description:
You are given a string s. Your task is to return the reversed version of the string.

Input:
    A single string s, where the length of s is between 1 and 1000.

Output:
    A single string that is the reverse of the input string.

Example:

    Input: "hello"
    Output: "olleh"
     
    Input: "Python"
    Output: "nohtyP"
"""

class StringQns_01:

    def __init__(self, raw_str: str):
        self.raw_str = raw_str

    def getReverseStr(self)->str:
        reverse_str = self.raw_str[::-1]
        print(reverse_str)
        return reverse_str