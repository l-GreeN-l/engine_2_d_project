from .shape import Shape

class Circle(Shape):

    name: str = "Circle"


    def __init__(self, x: int, y: int, radius: int):
        """

        :param x:
        :param y:
        """
        self.__radius = radius
        super().__init__(x=x, y=y)


    def draw(self):
        message = f""
        super().draw(self.name)

