from .shape import Shape
from .color import Color


class Rectangle(Shape):
    name: str = "Rectangle"

    __x: float
    __y: float

    def __init__(self, x: float, y: float, d1: float, d2: float):
        """
        (x, y) - coordinates of first point
        :param x:
        :param y:
        """

        self.__x = x
        self.__y = y
        self.__d1 = d1
        self.__d2 = d2
        self.__d3 = self.__d1
        self.__d4 = self.__d2

    def draw(self):
        message = f"({self.__x}, {self.__y}) with side {self.__d1}, {self.__d2}, {self.__d3}, {self.__d4}"
        super().draw(self.name, message=message)
