from shapes.circle import Circle
from shapes.color import Color
from engine2D import Engine2D
from math import sin, radians


class TestCicle:

    def test_simple_circle(self):
        """
        Check create circle
        :return:
        """
        x = 10
        y = 20
        radius = 22

        circle = Circle(radius=radius, x_centre=x, y_centre=y)

        x_, y_, radius_ = circle.get_parameters().values()

        assert x == x_
        assert y == y_
        assert radius == radius_

    def test_circle_negotive(self):
        """
        Check create with -radius
        :return:
        """
        x = 10
        y = 20
        radius = -22

        circle = Circle(radius=radius, x_centre=x, y_centre=y)

        assert not circle


    def test_circle_negotive2(self):
        """
        check create with 0 radius
        :return:
        """
        x = 10
        y = 20
        radius = 0

        circle = Circle(radius=radius, x_centre=x, y_centre=y)

        assert not circle

    def test_simple_circle_canvas(self):
        """
        Check create circle and copy, add to canvas and change color pen
        :return:
        """
        engine = Engine2D()

        x = 10
        y = 20
        radius = 22

        x2 = 100
        y2 = 200
        radius2 = 220

        circle = Circle(radius=radius, x_centre=x, y_centre=y)
        circle2 = Circle(radius=radius2, x_centre=x2, y_centre=y2)

        id1 = engine.add(circle)

        engine.set_color_pen(color=Color.green)

        id2 = engine.add(circle2)

        x_, y_, radius_ = engine.get_object_from_canvas(id_obj=id1).get_parameters().values()
        x2_, y2_, radius2_ = engine.get_object_from_canvas(id_obj=id2).get_parameters().values()

        assert x == x_
        assert y == y_
        assert radius == radius_

        assert x2 == x2_
        assert y2 == y2_
        assert radius2 == radius2_

        assert engine.get_object_from_canvas(id_obj=id1).get_color() == Color.black
        assert engine.get_object_from_canvas(id_obj=id2).get_color() == Color.green

    def test_simple_circle_canvas2(self):
        """
        Check create 2 circles, add to canvas and change color pen
        """
        engine = Engine2D()

        x = 10
        y = 20
        radius = 22

        circle = Circle(radius=radius, x_centre=x, y_centre=y)

        id1 = engine.add(circle)

        engine.set_color_pen(color=Color.green)

        id2 = engine.add(circle)

        x_, y_, radius_ = engine.get_object_from_canvas(id_obj=id1).get_parameters().values()
        x2_, y2_, radius2_ = engine.get_object_from_canvas(id_obj=id2).get_parameters().values()

        assert x == x_
        assert y == y_
        assert radius == radius_

        assert x == x2_
        assert y == y2_
        assert radius == radius2_

        assert engine.get_object_from_canvas(id_obj=id1).get_color() == Color.black
        assert engine.get_object_from_canvas(id_obj=id2).get_color() == Color.green
