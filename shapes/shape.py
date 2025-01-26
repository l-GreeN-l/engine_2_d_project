from tkinter import *


class Shape:

    __x: int
    __y: int

    def __init__(self, x, y):
        self.__x = x
        self.__y = y


    def draw(self, name, message):
        print(f"Drawing {name}: {message}")
