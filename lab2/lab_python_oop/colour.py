class FigureColor:

    #Инициализация свойства цвет
    def __init__(self):
        self._color = None

    #Получение цвета фигуры по обращению за ним
    @property
    def colorproperty(self):

        return self._color

    #Установка цвета фигуры
    @colorproperty.setter
    def colorproperty(self, value):

        self._color = value