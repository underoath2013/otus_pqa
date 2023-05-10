import pytest
from src.circle import Circle


def test_circle_perimeter_valid():
    valid_circle = Circle(1)
    assert valid_circle.perimeter == 6, 'Wrong circle perimeter'
    valid_circle.radius = 3
    assert valid_circle.perimeter == 18, 'Wrong circle perimeter'


def test_circle_area_valid():
    valid_circle = Circle(1)
    assert valid_circle.area == 3, 'Wrong circle area'
    valid_circle.radius = 3
    assert valid_circle.area == 28, 'Wrong circle area'


def test_circle_zero_side():  # радиус равен 0
    with pytest.raises(ValueError):
        Circle(0)


def test_circle_negative_side():  # радиус отрицательный
    with pytest.raises(ValueError):
        Circle(-1)
