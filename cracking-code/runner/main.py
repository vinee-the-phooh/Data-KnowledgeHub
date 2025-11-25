from src.pattern.SquareOfSideN import Pattern_01
from src.pattern.HollowSquare import Pattern_02
from src.pattern.RectanglePattern import Pattern_03
from src.function.CelsiusFahrenheit import function_01
from src.function.AreaOfRectangle import function_02
from src.listTupleDictionaries.SumofListElements import test_01
from src.stringQns.ReverseString import StringQns_01

if __name__ =="__main__":
    #Calling the method in SquareOfSideN 
    sq = Pattern_01(3)
    sq.print_pattern()

    sq = Pattern_02(5)
    sq.print_pattern()

    sq = Pattern_03(5,4)
    sq.print_pattern()

    fn = function_01(23)
    fn.convert()

    fn =   fn = function_02(4,5)
    fn.getArea()

    numbers = [1,-9,20, -100]
    test = test_01(numbers)
    test.get_sum()

    strQn  = StringQns_01("Data")
    strQn.getReverseStr()




    