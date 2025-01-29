from .shape import Shape
from math import sin, radians


class Triangle(Shape):
    name: str = "Triangle"

    __x: float
    __y: float

    __angle: float
    __angle1: float
    __angle2: float

    def __new__(cls, *args, **kwargs):
        if len(kwargs) > 0 or len(args) > 0:
            if (kwargs.get('angle1') > 0 and kwargs.get('angle2') > 0 and
                    kwargs.get('angle2') + kwargs.get('angle1') < 180 and kwargs.get('delta1') > 0):
                return super().__new__(cls)
            else:
                print('Error in arguments')
        else:
            return super().__new__(cls)

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

    def get_parameters(self):
        return {
            "x": self.__x, "y": self.__y,
            "angle1": self.__angle1, "angle2": self.__angle2, "angle3": self.__angle3, "angle": self.__angle,
            "delta1": self.__delta1, "delta2": self.__delta2, "delta3": self.__delta3
        }

    def draw(self):
        message = (f" first point - ({self.__x}, {self.__y})"
                   f" with angles({self.__angle1}, {self.__angle2}, {self.__angle3})"
                   f" and lengths ({self.__delta1}, {self.__delta2}, {self.__delta3})"
                   )
        super().draw(self.name, message=message)
