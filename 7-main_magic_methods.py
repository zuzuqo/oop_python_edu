class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
        if self.MIN_COORD <= y <= self.MAX_COORD:
            self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left

    # когда создается новый атрибут класса
    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError('доступ запрещен')
        else:
            return object.__getattribute__(self, item)

    # когда изменяется атрибут key (идет присвоение значение к атрибуту)
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('недопустимое имя атрибута')
        else:
            object.__setattr__(self, key, value)

    # когда обращаются к несуществующему атрибуту класса
    def __getattr__(self, item):
        return False

    # когда удаляется атрибут
    def __delattr__(self, item):
        print('__delattr__: ' + item)
        object.__delattr__(self, item)


pt = Point(1, 2)
a = pt.y
del pt.x
print(a)
