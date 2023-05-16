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

    @property
    def perimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter

    @property
    def half_perimeter(self):
        half_perimeter = self.perimeter / 2
        return half_perimeter

    @property
    def area(self):
        area = int((self.half_perimeter * (self.half_perimeter - self.a) *
                   (self.half_perimeter - self.b) * (self.half_perimeter - self.c)) ** 0.5)
        return area
