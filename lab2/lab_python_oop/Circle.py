from lab_python_oop.figure import Figure
from lab_python_oop.colour import FigureColor
import math


class Circle(Figure):

    Figure_type = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.Figure_type

    def __init__(self,_color_param,_radius_param):

        self._radius = _radius_param
        self.fcolor = FigureColor()
        self.fcolor.colorproperty = _color_param

    def yardage(self):
        return math.pi*(self._radius)**2


    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.\n'.format(
            Circle.get_figure_type(),
            self.fcolor.colorproperty,
            self._radius,
            self.yardage()
        )