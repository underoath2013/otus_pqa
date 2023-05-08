from src.figure import Figure


class Triangle(Figure):
    """
    Класс для вычисления периметра и площади (формула Герона) треугольника
    """

    def __init__(self, a: int, b: int, c: int) -> None:
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError('Invalid triangle')
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.perimeter = a + b + c
        p = int(self.perimeter / 2)  # полупериметр
        self.area = int(
            (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5)
