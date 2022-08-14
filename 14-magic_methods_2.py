# 14
class Clock:
    __DAY = 24 * 60 * 60  # Число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Секунды должны быть целым числом')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = self.seconds // 60 % 60
        h = self.seconds // 60 // 60 % 24
        return f'{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}'

    @classmethod
    def __to_seconds(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Тип данных должен быть int или Clock')
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return sc

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')

    # сложение
    def __add__(self, other):
        sc = self.__to_seconds(other)
        return Clock(self.seconds + sc)

    # отвечает за формат с1 = 100 + с2 (при этои создается новый экземпляр, а не изменяется старый)
    def __radd__(self, other):
        return self + self.__to_seconds(other)

    # с этим методом при вызове операции c1 += 100, например, не создается новый экземпляр класса, а изменяется старый
    def __iadd__(self, other):
        sc = self.__to_seconds(other)
        self.seconds += sc
        return self

    # вычитание
    def __sub__(self, other):
        sc = self.__to_seconds(other)
        return Clock(self.seconds - sc)

    # отвечает за формат с1 = 100 - с2 (при этои создается новый экземпляр, а не изменяется старый)
    def __rsub__(self, other):
        sc = self.__DAY - self.seconds + other
        return Clock(sc)

    # с этим методом при вызове операции c1 -= 100, например, не создается новый экземпляр класса, а изменяется старый
    def __isub__(self, other):
        sc = self.__to_seconds(other)
        self.seconds -= sc
        return self

    # умножение
    def __mul__(self, other):
        sc = self.__to_seconds(other)
        return Clock(self.seconds * sc)

    # отвечает за формат с1 = 100 * с2 (при этои создается новый экземпляр, а не изменяется старый)
    def __rmul__(self, other):
        return self + self.__to_seconds(other)

    # с этим методом при вызове операции c1 *= 100, например, не создается новый экземпляр класса, а изменяется старый
    def __imul__(self, other):
        sc = self.__to_seconds(other)
        self.seconds *= sc
        return self

# 15
    # проверка на равенство (неравенство реализовывается по умолчанию)
    def __eq__(self, other):
        sc = self.__to_seconds(other)
        return self.seconds == sc

    # проверка на < (проверка на > реализуется по умолчанию)
    def __lt__(self, other):
        sc = self.__to_seconds(other)
        return self.seconds < sc

    # проверка на >
    def __gt__(self, other):
        sc = self.__to_seconds(other)
        return self.seconds > sc

    # проверка на <=
    def __le__(self, other):
        sc = self.__to_seconds(other)
        return self.seconds <= sc

    # проверка на >=
    def __ge__(self, other):
        sc = self.__to_seconds(other)
        return self.seconds >= sc

c1 = Clock(1000)
print(c1)
print(c1.get_time())
c2 = Clock(2000)
c1 = 100 + c2
print(c1)
c1 += 1000
print(c1.get_time())
print(c1)
print(f'c1 == Clock(2000) is {c1 == Clock(2000)}')
print(f'c2 == Clock(2000) is {c2 == Clock(2000)}')
print(f'c1 >= Clock(2000) is {c1 >= Clock(2000)}')
print(f'c1 > Clock(2000) is {c1 > Clock(2000)}')
print(f'c2 <= Clock(2000) is {c2 <= Clock(2000)}')
print(f'c2 < Clock(2000) is {c2 < Clock(2000)}')
