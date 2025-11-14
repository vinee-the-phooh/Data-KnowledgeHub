from src.pattern.SquareOfSideN import Pattern_01
from src.pattern.HollowSquare import Pattern_02

if __name__ =="__main__":
    #Calling the method in SquareOfSideN 
    sq = Pattern_01(3)
    sq.print_pattern()

    sq = Pattern_02(5)
    sq.print_pattern()

    