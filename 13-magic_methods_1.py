class Cat:
    def __init__(self, name):
        self.name = name

    # для отображения информации об объекте класса в режиме отладки
    def __repr__(self):
        return f'{self.__class__}: {self.name}'

    # для отображения информации об объекте класса для пользователей
    def __str__(self):
        return f'{self.name}'


cat = Cat('Маруся')
print(cat)


class Point:
    def __init__(self, *args):
        self.__coords = args

    # позволяет применять функцию len к экземплярам класса
    def __len__(self):
        return len(self.__coords)

    # позволяет применять функцию abs к экземплярам класса
    def __abs__(self):
        return list(map(abs, self.__coords))


p = Point(1, -2, -50)
print(len(p))
print(abs(p))
