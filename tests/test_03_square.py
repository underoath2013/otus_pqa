import pytest
from src.square import Square


def test_square_perimeter_valid():
    valid_square = Square(2)
    assert valid_square.perimeter == 8, 'Wrong square perimeter'


def test_square_area_valid():
    valid_square = Square(2)
    assert valid_square.area == 4, 'Wrong square area'


def test_square_zero_side():  # сторона квадрата равна 0
    with pytest.raises(ValueError):
        Square(0)


def test_square_negative_side():  # сторона квадрата отрицательная
    with pytest.raises(ValueError):
        Square(-1)



