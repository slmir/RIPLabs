from lab_python_oop.Rectangle import Rectangle


class Sqaure(Rectangle):


    Figure_type = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.Figure_type

    def __init__(self, _color_param,_a_param):

        self._a = _a_param
        super().__init__(_color_param,_a_param,_a_param)

    def __repr__(self):
        return '{} {} цвета со стороной {} и площадью {}.\n'.format(
            Sqaure.get_figure_type(),
            self.fcolor.colorproperty,
            self._a,
            self.yardage()
        )