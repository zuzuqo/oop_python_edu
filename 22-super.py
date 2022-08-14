class Geom:
    def __init__(self, x1, x2, y1, y2):
        print(f'Geom - {self.__class__}')
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print('Line - draw')


class Rect(Geom):
    def __init__(self, x1, x2, y1, y2, fill=None):
        super().__init__(x1, x2, y1, y2)
        print('Rect - init')
        self.fill = fill

    def draw(self):
        print('Rect - draw')


l = Line(1, 2, 10, 20)
r = Rect(1, 2, 10, 20)
