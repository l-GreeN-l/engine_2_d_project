from shapes.rectangle import Rectangle
from shapes.color import Color
from engine2D import Engine2D


class TestRectangle:

    def test_simple_rectangle(self):
        """
        Simple check create rectangle
        :return:
        """
        x = 5
        y = 10
        d1 = 50
        d2 = 100

        d3 = d1
        d4 = d2

        rectangle = Rectangle(x=x, y=y, d1=d1, d2=d2)

        x_, y_, d1_, d2_, d3_, d4_ = rectangle.get_parameters().values()
        assert x == x_
        assert y == y_
        assert d1 == d1_
        assert d2 == d2_
        assert d3 == d3_
        assert d4 == d4_

    def test_negotive_rectangle(self):
        """
        Simple check negotive event
        :return:
        """
        x = 5
        y = 10
        d1 = 0
        d2 = 0

        rectangle = Rectangle(x=x, y=y, d1=d1, d2=d2)

        assert not rectangle


    def test_canvas_rectangle(self):
        """
        1 reactangle witch copy and canvas check
        :return:
        """
        engine = Engine2D()

        x = 5
        y = 10
        d1 = 50
        d2 = 100

        d3 = d1
        d4 = d2

        rectangle = Rectangle(x=x, y=y, d1=d1, d2=d2)
        id1 = engine.add(rectangle)
        x_, y_, d1_, d2_, d3_, d4_ = engine.get_object_from_canvas(id_obj=id1).get_parameters().values()

        assert x == x_
        assert y == y_
        assert d1 == d1_
        assert d2 == d2_
        assert d3 == d3_
        assert d4 == d4_

        assert engine.get_object_from_canvas(id_obj=id1).get_color() == Color.black

        engine.set_color_pen(Color.yellow)

        id2 = engine.add(rectangle)

        assert engine.get_object_from_canvas(id_obj=id1).get_color() == Color.black
        assert engine.get_object_from_canvas(id_obj=id2).get_color() == Color.yellow


    def test_canvas_rectangle2(self):
        """
        2 rectangle and canvas check
        :return:
        """
        engine = Engine2D()

        x = 5
        y = 10
        d1 = 50
        d2 = 100

        d3 = d1
        d4 = d2

        x2 = 5
        y2 = 10
        d12 = 50
        d22 = 100

        d32 = d12
        d42 = d22

        rectangle = Rectangle(x=x, y=y, d1=d1, d2=d2)
        rectangle2 = Rectangle(x=x2, y=y2, d1=d12, d2=d22)
        id1 = engine.add(rectangle)
        x_, y_, d1_, d2_, d3_, d4_ = engine.get_object_from_canvas(id_obj=id1).get_parameters().values()

        assert x == x_
        assert y == y_
        assert d1 == d1_
        assert d2 == d2_
        assert d3 == d3_
        assert d4 == d4_

        assert engine.get_object_from_canvas(id_obj=id1).get_color() == Color.black

        engine.set_color_pen(Color.yellow)

        id2 = engine.add(rectangle2)

        assert engine.get_object_from_canvas(id_obj=id1).get_color() == Color.black
        assert engine.get_object_from_canvas(id_obj=id2).get_color() == Color.yellow

        x2_, y2_, d12_, d22_, d32_, d42_ = engine.get_object_from_canvas(id_obj=id2).get_parameters().values()

        assert x2 == x2_
        assert y2 == y2_
        assert d12 == d12_
        assert d22 == d22_
        assert d32 == d32_
        assert d42 == d42_
