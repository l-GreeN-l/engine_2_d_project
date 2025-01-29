from shapes.triangle import Triangle
from shapes.color import Color
from engine2D import Engine2D
from math import sin, radians


class TestTriangle:

    def test_simple_triangle(self):
        """
        Simple check create triangle
        :return:
        """
        x = 10
        y = 30
        angle = 30

        angle1 = 50
        angle2 = 50
        angle3 = 80

        delta1 = 6
        delta2 = delta1 * sin(radians(angle1)) / sin(radians(angle3))
        delta3 = delta2 * sin(radians(angle2)) / sin(radians(angle1))

        triangle = Triangle(x=x, y=y, angle=angle, angle1=angle1, angle2=angle2, delta1=delta1)

        x_, y_, angle1_, angle2_, angle3_, angle_, delta1_, delta2_, delta3_ = triangle.get_parameters().values()

        assert x == x_
        assert y == y_
        assert angle_ == angle_
        assert angle1_ == angle1
        assert angle2_ == angle2
        assert angle3_ == angle3

        assert delta1_ == delta1
        assert delta2_ == delta2
        assert delta3_ == delta3

    def test_triangle_negotive_angle(self):
        """
        Simple check negotive event triangle
        :return:
        """
        x = 10
        y = 30
        angle = 30

        angle1 = 50
        angle2 = 150

        delta1 = 6

        triangle = Triangle(x=x, y=y, angle=angle, angle1=angle1, angle2=angle2, delta1=delta1)

        assert not triangle

    def test_triangle_negotive_angle2(self):
        """
        Simple check negotive event triangle
        :return:
        """
        x = 10
        y = 30
        angle = 30

        angle1 = -50
        angle2 = 100

        delta1 = 6

        triangle = Triangle(x=x, y=y, angle=angle, angle1=angle1, angle2=angle2, delta1=delta1)

        assert not triangle

    def test_triangle_negotive_long(self):
        """
        Simple check negotive event triangle
        :return:
        """
        x = 10
        y = 30
        angle = 30

        angle1 = 50
        angle2 = 100

        delta1 = -6

        triangle = Triangle(x=x, y=y, angle=angle, angle1=angle1, angle2=angle2, delta1=delta1)

        assert not triangle

    def test_canvas_triangle(self):
        """
        Test add 1 triangle and it copy to canvas and change color
        """
        x = 10
        y = 30
        angle = 30

        angle1 = 50
        angle2 = 50
        angle3 = 80

        delta1 = 6
        delta2 = delta1 * sin(radians(angle1)) / sin(radians(angle3))
        delta3 = delta2 * sin(radians(angle2)) / sin(radians(angle1))

        engine = Engine2D()

        triangle = Triangle(x=x, y=y, angle=angle, angle1=angle1, angle2=angle2, delta1=delta1)

        id1 = engine.add(triangle)

        x_, y_, angle1_, angle2_, angle3_, angle_, delta1_, delta2_, delta3_ = triangle.get_parameters().values()

        assert x == x_
        assert y == y_
        assert angle_ == angle_
        assert angle1_ == angle1
        assert angle2_ == angle2
        assert angle3_ == angle3

        assert delta1_ == delta1
        assert delta2_ == delta2
        assert delta3_ == delta3


        assert engine.get_object_from_canvas(id_obj=id1).get_color() == Color.black

        engine.set_color_pen(Color.yellow)

        id2 = engine.add(triangle)

        assert engine.get_object_from_canvas(id_obj=id1).get_color() == Color.black
        assert engine.get_object_from_canvas(id_obj=id2).get_color() == Color.yellow


    def test_triangle_canvas_2(self):
        """
        Test add 2 triangle to canvas and change color
        :return:
        """
        x = 10
        y = 30
        angle = 30

        angle1 = 50
        angle2 = 50
        angle3 = 80

        delta1 = 6
        delta2 = delta1 * sin(radians(angle1)) / sin(radians(angle3))
        delta3 = delta2 * sin(radians(angle2)) / sin(radians(angle1))

        x2 = 40
        y2 = 30
        angle_2 = 30

        angle1_2 = 40
        angle2_2 = 30
        angle3_2 = 110

        delta1_2 = 15
        delta2_2 = delta1_2 * sin(radians(angle1_2)) / sin(radians(angle3_2))
        delta3_2 = delta2_2 * sin(radians(angle2_2)) / sin(radians(angle1_2))

        engine = Engine2D()

        triangle = Triangle(x=x, y=y, angle=angle, angle1=angle1, angle2=angle2, delta1=delta1)
        triangle2 = Triangle(x=x2, y=y2, angle=angle_2, angle1=angle1_2, angle2=angle2_2, delta1=delta1_2)

        id1 = engine.add(triangle)

        x_, y_, angle1_, angle2_, angle3_, angle_, delta1_, delta2_, delta3_ = engine.get_object_from_canvas(
            id_obj=id1
        ).get_parameters().values()

        assert x == x_
        assert y == y_
        assert angle_ == angle_
        assert angle1_ == angle1
        assert angle2_ == angle2
        assert angle3_ == angle3

        assert delta1_ == delta1
        assert delta2_ == delta2
        assert delta3_ == delta3

        assert engine.get_object_from_canvas(id_obj=id1).get_color() == Color.black

        engine.set_color_pen(Color.orange)
        id2 = engine.add(triangle2)

        assert engine.get_object_from_canvas(id_obj=id2).get_color() == Color.orange

        x2_, y2_, angle1_2_, angle2_2_, angle3_2_, angle_2_, delta1_2_, delta2_2_, delta3_2_ = engine.get_object_from_canvas(
            id_obj=id2
        ).get_parameters().values()

        assert x2 == x2_
        assert y2 == y2_
        assert angle_2 == angle_2_
        assert angle1_2 == angle1_2_
        assert angle2_2 == angle2_2_
        assert angle3_2 == angle3_2_

        assert delta1_2 == delta1_2_
        assert delta2_2 == delta2_2_
        assert delta3_2 == delta3_2_