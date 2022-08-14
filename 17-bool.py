class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return self.x ** 2 + self.y ** 2

    def __bool__(self):
        return self.x != 0 and self.y != 0


p = Point(0, 0)
print(bool(p))

