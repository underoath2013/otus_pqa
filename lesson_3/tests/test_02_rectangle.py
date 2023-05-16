import pytest
from src.rectangle import Rectangle


def test_rectangle_perimeter_valid():
    valid_rectangle = Rectangle(2, 5)
    assert valid_rectangle.perimeter == 14, 'Wrong rectangle perimeter'
    valid_rectangle.a = 3
    valid_rectangle.b = 6
    assert valid_rectangle.perimeter == 18, 'Wrong rectangle perimeter'


def test_rectangle_area_valid():
    valid_rectangle = Rectangle(2, 5)
    assert valid_rectangle.area == 10, 'Wrong rectangle area'
    valid_rectangle.a = 3
    valid_rectangle.b = 6
    assert valid_rectangle.area == 18, 'Wrong rectangle area'


def test_rectangle_zero_side():  # одна из сторон прямоугольника равна 0
    with pytest.raises(ValueError):
        Rectangle(0, 2)


def test_rectangle_negative_side():  # одна из сторон прямоугольника отрицательная
    with pytest.raises(ValueError):
        Rectangle(-1, 2)
