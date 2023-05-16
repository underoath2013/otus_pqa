from src.rectangle import Rectangle


class Square(Rectangle):
    """
    Класс для вычисления периметра и площади квадрата.
    Вместо задания двух сторон прямоугольника мы передаем
    одну сторону и используем ее дважды для создания квадрата.
    Кроме того, мы не определяем новые атрибуты area и perimeter,
    потому что они уже определены в классе Rectangle и наследуются в класс Square.
    """

    def __init__(self, a: int) -> None:
        if a <= 0:
            raise ValueError('Invalid square')
        self.a = int(a)

    @property
    def b(self):
        return self.a

    @b.setter
    def b(self, value):
        self.a = value
