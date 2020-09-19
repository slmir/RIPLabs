from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Sqare import Sqaure
import numpy as np


def main():
    r = Rectangle("синего", 11, 11)
    c = Circle("зеленого",11)
    sq = Sqaure("красного",11)
    print(r)
    print(c)
    print(sq)
    a = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]],int)
    print(a)


if __name__ == "__main__":
    main()
