class Point:
    __slots__ = ('x', 'y', '__length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = (x ** 2 + y ** 2) ** 0.5

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value


p = Point(10, 20)
print(p.length)


class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point2D):
    # Point3D не наследует коллекцию slots у Point2D
    pass


p3d = Point3D(1, 2)
p3d.z = 3                           # Point3D не наследует коллекцию slots у Point2D

print(p3d.__dict__)                 # при этом свойтсва p3d.x p3d.y не попадают в коллекцию dict
print(p3d.x, p3d.y, p3d.z)

del p3d.x                           # при этом можно удалять
p3d.x = 10                          # создавать
print(p3d.__dict__)                 # p3d.x и p3d.y не попадут в коллекцию dict всё равно
print(p3d.x, p3d.y, p3d.z)          # но всё будет в порядке


class Point3DDD(Point2D):
    __slots__ = 'z',                # slots является коллекцией



