import pytest
from src.triangle import Triangle


def test_triangle_perimeter_valid():
    valid_triangle = Triangle(13, 14, 15)
    assert valid_triangle.perimeter == 42, 'Wrong triangle perimeter'
    valid_triangle.a = 16
    valid_triangle.b = 17
    valid_triangle.c = 18
    assert valid_triangle.perimeter == 51, 'Wrong triangle perimeter'


def test_triangle_area_valid():
    valid_triangle = Triangle(13, 14, 15)
    assert valid_triangle.area == 84, 'Wrong triangle area'
    valid_triangle.a = 16
    valid_triangle.b = 17
    valid_triangle.c = 18
    assert valid_triangle.area == 124, 'Wrong triangle area'


def test_triangle_area_equilateral_triangle():  # равносторонний треугольник
    equilateral_triangle = Triangle(10, 10, 10)
    assert equilateral_triangle.area == 43, 'Wrong equilateral triangle area'


def test_triangle_area_right_triangle():  # прямоугольный треугольник
    right_triangle = Triangle(3, 4, 5)
    assert right_triangle.area == 6, 'Wrong right triangle area'


def test_triangle_zero_side():  # одна из сторон треугольника равна 0
    with pytest.raises(ValueError):
        Triangle(0, 14, 15)


def test_triangle_negative_side():  # одна из сторон треугольника отрицательная
    with pytest.raises(ValueError):
        Triangle(13, 14, -15)


def test_triangle_not_triangle():  # заданные стороны не образуют треугольник
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)
