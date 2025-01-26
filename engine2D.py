from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.triangle import Triangle
from shapes.shape import Shape

class Engine2D():

    __canvas: dict

    def __init__(self):
        self.__canvas = {}

    def add(self, item: Shape):
        if type(item == Shape) and item != None:
            self.__canvas.update({id(item): item})
        else:
            raise TypeError('Need Shape')

    def clear(self):
        self.__canvas = {}

    def get_canvas(self):
        return self.__canvas.copy()

    def get_object_from_canvas(self, id_obj):
        return self.__canvas.get(id_obj)

    def draw(self):

        for item in self.__canvas:
            item.draw()

        self.clear()




