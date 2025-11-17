"""
Problem Description:

You are given a temperature in Celsius. 
Your task is to convert it to Fahrenheit and return the result.

Formula:
To convert Celsius to Fahrenheit, use the formula:
F = (9/5 * C) + 32
Where F is the temperature in Fahrenheit and C is the temperature in Celsius.

Input:
    A floating-point number C representing the temperature in Celsius.
Output:
    A floating-point number representing the temperature in Fahrenheit.
Example:
    Input: C = 25
    Output: 77.0
     
    Input: C = 0
    Output: 32.0
"""

class function_01:

    def __init__(self,value : float):
        self.value = value

    def convert(self) ->float:
        temperature = (9/5 *(self.value)) +32
        print(f"The temperature in Celsius {self.value} and The temperature in Fahrenheit {temperature}")
        return temperature