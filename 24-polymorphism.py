class Figure:
    def get_pr(self):

        raise NotImplementedError('В дочернем классе должен быть определен метод get_pr')


class Square(Figure):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return self.a * 4


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_pr(self):
        return self.a * 2 + self.b * 2


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c


geom = [
    Rectangle(1, 2), Rectangle(3, 4),
    Square(10), Square(20),
    Triangle(1, 2, 3), Triangle(10, 20, 30)
]

for i in geom:
    print(i.get_pr())

print(Rectangle(1, 2).__dict__)
