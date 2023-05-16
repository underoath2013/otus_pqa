class Figure:
    def __init__(self, name: str) -> None:
        self.name = name

    def add_area(self, figure: 'Figure') -> int:
        if not isinstance(figure, Figure):
            raise ValueError('Invalid figure')
        return self.area + figure.area
