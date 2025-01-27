from .shape import Shape
from math import sin, radians
from .color import Color


class Triangle(Shape):
    name: str = "Triangle"

    __x: float
    __y: float

    __angle: float
    __angle1: float
    __angle2: float

    def __new__(cls, angle: float, angle1: float, angle2: float, delta1: float, *args, **kwargs):

        if (angle1 > 0 and angle2 > 0 and (angle2 + angle1) < 180 and delta1 > 0) > 0:
            return super().__new__(cls)
        else:
            print('Error in arguments')

    def __init__(self, x: int, y: int, angle: float, angle1: float, angle2: float, delta1: float):
        """
        Angles in grads
        (x, y): coordinates of first point

        :param angle: first angle between 0 and first line (0-360)
        :param angle1: angle between first line and second line
        :param angle2: angle between second line and third line
        :param length1: length of first line
        :param length2: length of second line
        :param length3: length of third line
        """
        self.__x = x
        self.__y = y

        self.__angle = angle
        self.__angle1 = angle1
        self.__angle2 = angle2

        self.__delta1 = delta1

        self.__angle3 = 180 - self.__angle1 - self.__angle2
        self.__delta2 = self.__delta1 * sin(radians(self.__angle1)) / sin(radians(self.__angle3))
        self.__delta3 = self.__delta2 * sin(radians(self.__angle2)) / sin(radians(self.__angle1))

    def draw(self):
        message = (f" first point - ({self.__x}, {self.__y})"
                   f" with angles({self.__angle1}, {self.__angle2}, {self.__angle3})"
                   f" and lengths ({self.__delta1}, {self.__delta2}, {self.__delta3})"
                   )
        super().draw(self.name, message=message)
