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
        self.area = a * b
        self.perimeter = 2 * (a + b)

