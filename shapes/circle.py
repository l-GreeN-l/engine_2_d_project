from .shape import Shape
from .color import Color


class Circle(Shape):
    name: str = "Circle"

    __x: float
    __y: float

    def __new__(cls, *args, **kwargs):

        if len(kwargs) > 0 or len(args) > 0:
            if kwargs.get('radius') > 0:
                return super().__new__(cls)
            else:
                print('Error - radius <= 0')
        else:
            return super().__new__(cls)

    def __init__(self, x_centre: float, y_centre: float, radius: float):

        """
        (x, y) - centre coordinates
        :param x:
        :param y:
        """
        self.__radius = radius
        self.__x = x_centre
        self.__y = y_centre

    def draw(self):
        message = f"({self.__x}, {self.__y}) with radius {self.__radius}"
        super().draw(self.name, message=message)

    def get_parameters(self):
        return {
            "x": self.__x, "y": self.__y, "radius": self.__radius
        }

