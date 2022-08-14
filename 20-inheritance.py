class Geom:
    name = 'Geom'

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print('Drawing line')


class Rect(Geom):
    def draw(self):
        print('Drawing rect')


r = Rect()
print(r.name)

l = Line()
print(l.name)

r.set_coords(1, 2, 3, 4)
l.set_coords(1, 2, 3, 4)

print(issubclass(Line, object))