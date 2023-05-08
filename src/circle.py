from src.figure import Figure
from math import pi


class Circle(Figure):
    """
    Класс для вычисления длины окружности и площади круга
    """

    def __init__(self, radius: int) -> None:
        if radius <= 0:
            raise ValueError('Invalid circle')
        self.radius = int(radius)
        self.area = int(pi * (radius ** 2))
        self.perimeter = int(2 * pi * radius)
