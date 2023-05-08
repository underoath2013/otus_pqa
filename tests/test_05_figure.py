import pytest
from src.figure import Figure
from src.triangle import Triangle
from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle


def test_figure_init():
    figure = Figure("Test")
    assert figure.name == "Test"


def test_figure_add_area():
    figure1 = Figure("Figure1")
    figure2 = Figure("Figure2")
    figure1.area = 10
    figure2.area = 20
    assert figure1.add_area(figure2) == 30


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


