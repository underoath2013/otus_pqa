from src.figure import Figure


class Rectangle(Figure):
    """
    Класс для вычисления периметра и площади прямоугольника
    """

    def __init__(self, a: int, b: int) -> None:
        if a <= 0 or b <= 0:
            raise ValueError('Invalid rectangle')
        self.a = int(a)
        self.b = int(b)

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return 2 * (self.a + self.b)
