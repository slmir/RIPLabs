from lab_python_oop.figure import Figure
from lab_python_oop.colour import FigureColor


class Rectangle(Figure):


    Figure_type = "Прямоугольник"

    #Cls - ссылка на весь класс
    @classmethod
    def get_figure_type(cls):
        return cls.Figure_type

    #Инициализация параметров фигуры
    def __init__(self, _colour_param, _a_param, _b_param):

        self._a = _a_param
        self._b = _b_param
        self.fcolor = FigureColor()
        self.fcolor.colorproperty = _colour_param

    #Вычисление площади фигуры
    def yardage(self):
        return self._a*self._b

    #Получение свойств фигуры
    def __repr__(self):
        return '\n{} {} цвета высотой {} и шириной {} и площадью {}.\n'.format(
            Rectangle.get_figure_type(),
            self.fcolor.colorproperty,
            self._a,
            self._b,
            self.yardage()
        )
        #return '{} '.format(Rectangle.get_figure_type()), ' {} '.format(self.fcolor.colorproperty), ' цвета, высотой {} '.format(
        #    self._a), ' и шириной {} '.format(self._b), ', с площадью {}'.format(self.yardage())