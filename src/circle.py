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

    @property
    def area(self):
        return int(pi * (self.radius ** 2))

    @property
    def perimeter(self):
        return int(2 * pi * self.radius)
