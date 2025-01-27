from tkinter import *
from enum import Enum
from . color import Color

class Shape:

    def set_color(self, color):
        if type(color) == Color:
            self.__color = color
        else:
            print('Error color')
            self.__color = Color.black

    def draw(self, name, message):
        print(f"Drawing {name}: {message}, color = {self.get_color().value}")

    def get_color(self):
        return self.__color
