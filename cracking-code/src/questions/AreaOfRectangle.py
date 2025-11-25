"""
Problem Description:

You are given the length and breadth of a rectangle. 
Your task is to compute and return the area of the rectangle.

Formula:
To calculate the area of a rectangle:
Area=length×breadth

Input:
    Two floating-point numbers, length and breadth, representing the dimensions of the rectangle.

Output:
    A floating-point number representing the area of the rectangle.

Example:
    Input: length = 5, breadth = 3
    Output: 15.0
     
    Input: length = 7.5, breadth = 2.4
    Output: 18.0
"""

class function_02:

    def __init__(self,length: float,breadth: float ):
         if not isinstance(breadth, (int,float)):
             raise TypeError("Length should be a number")
         
         if not isinstance(length, (int, float)):
             raise TypeError("length should be a number")
         self.length = length
         self.breadth = breadth

    def getArea(self):
        area = self.length* self.breadth
        print(area)
        return area


    