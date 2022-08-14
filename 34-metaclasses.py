A = type('Point', (), {'MAX_COORD': 100, 'MIN_COORD': 0})

# выше создается ссылка на экземпляр класса Point
# class Point:
#     MAX_COORD = 100
#     MIN_COORD = 0


print(type(A))
print(A.__dict__)

pt = A()
print(pt.MAX_COORD)


class B1: pass


class B2: pass


# тут создается ссылка на класс Point2, который наследуется от B1 и B2
B = type('Point2', (B1, B2), {'MAX_COORD': 100, 'MIN_COORD': 0})
print(B.__mro__)


def method1(self):
    print(self.__dict__)


# динамическое создание класса Point3 с сылкой С на него и добавление функции
C = type('Point3', (B1, B2), {'MAX_COORD': 100, 'method1': method1})
pt = C()
pt.method1()

# динамическое создание класса Point4 с сылкой D на него и добавление функции с помощью лямбда-функции
D = type('Point4', (B1, B2), {'MAX_COORD': 100, 'method1': lambda self: print(f'D - MAX_COORD = {self.MAX_COORD}')})
pt = D()
pt.method1()
