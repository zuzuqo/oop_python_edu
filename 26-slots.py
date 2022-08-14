import time
import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


class Point2D:
    # не позволяет свободно работать с другими свойствами и создавать новые
    # увеличивает скорость работы с элементами slots
    # и уменьшает размер занимаемой памяти
    __slots__ = ('x', 'y')

    MAX_COORD = 100             # это свойство в режиме read-only

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


p = Point2D(10, 20)
p2 = Point(10, 20)

print(p.x, p.y)
print(p.MAX_COORD)

# это вызывает ошибки
# p.MAX_COORD = 1000
# p.z = 30


t1 = timeit.timeit(p.calc)      # Point2D
t2 = timeit.timeit(p2.calc)     # Point
print(t1, t2)
