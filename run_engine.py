from engine2D import Engine2D
from shapes.circle import Circle
from shapes.triangle import Triangle
from shapes.rectangle import Rectangle
from shapes.color import Color

engine = Engine2D()

circle_red = Circle(x_centre=-1, y_centre=0, radius=5)
circle_w = Circle(x_centre=0, y_centre=0, radius=10)
rectangle = Rectangle(x=20, y=-30, d1=10, d2=5)
triangle = Triangle(x=0, y=-6, angle=0, angle1=50, angle2=129, delta1=6)

engine.set_color_pen(Color.green)

engine.add(circle_red)
engine.add(circle_w)

engine.set_color_pen(Color.orange)

engine.add(rectangle)
engine.add(triangle)

engine.draw()

engine.add(rectangle)
engine.add(triangle)

engine.set_color_pen(Color.yellow)

engine.add(circle_red)
engine.add(circle_w)

engine.draw()