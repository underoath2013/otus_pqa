import pytest
from src.figure import Figure
from src.triangle import Triangle
from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle


def test_figure_add_area_invalid_argument():
    figure = Figure("Test")
    with pytest.raises(ValueError):
        figure.add_area("Invalid")


def test_triangle_and_square_add_area():
    square = Square(10)
    triangle = Triangle(13, 14, 15)
    assert triangle.add_area(square) == 184


def test_rectangle_and_circle_add_area():
    circle = Circle(1)
    rectangle = Rectangle(2, 5)
    assert circle.add_area(rectangle) == 13
