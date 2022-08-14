class Geom:
    name = 'Geom'

    def __init__(self, x1, x2, y1, y2):
        print(f'Geom - {self.__class__}')
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    def _verify_coord(self, coord):
        if 0 <= coord < 100:
            raise AttributeError


class Rect(Geom):
    def __init__(self, x1, x2, y1, y2, fill='red'):
        super().__init__(x1, x2, y1, y2)
        self._verify_coord(x1)
        self._verify_coord(y1)
        self._verify_coord(x2)
        self._verify_coord(y2)
        self.__fill = fill

    def get_coords(self):
        return (self._x1, self._y1)


r = Rect(1, 2, 10, 200)
print(r.get_coords())
print(r.__dict__)
