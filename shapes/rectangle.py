from .shape import Shape


class Rectangle(Shape):
    name: str = "Rectangle"

    __x: float
    __y: float

    def __new__(cls, *args, **kwargs):
        if len(kwargs) > 0 or len(args) > 0:
            if kwargs.get('d1') != 0 and kwargs.get('d2') != 0:

                return super().__new__(cls)
            else:
                print('Error - d1 or d1 = 0')
        else:
            return super().__new__(cls)

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

    def get_parameters(self):
        return {
            "x": self.__x, "y": self.__y,
            "d1": self.__d1, "d2": self.__d2, "d3": self.__d3, "d4": self.__d4
        }
