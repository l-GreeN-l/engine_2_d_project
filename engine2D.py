from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.triangle import Triangle
from shapes.shape import Shape
from shapes.color import Color


class Engine2D:
    __color_pen: Color = Color.black
    __canvas_list: dict

    def __init__(self):
        self.__canvas_list = {}

    def add(self, item: Shape):
        if type(item == Shape) and item != None:
            item.set_color(self.__color_pen)
            self.__canvas_list.update({id(item): item})

    def __clear(self):
        self.__canvas_list = {}

    def get_canvas(self):
        return self.__canvas_list.copy()

    def get_object_from_canvas(self, id_obj):
        return self.__canvas_list.get(id_obj)

    def draw(self):
        for item in self.__canvas_list.values():
            if type(item == Shape):
                item.draw()
            else:
                continue

        self.__clear()

    def set_color_pen(self, color: Color):
        if type(color) == Color:
            self.__color_pen = color
        else:
            print('color empty')
            self.__color_pen = Color.black
