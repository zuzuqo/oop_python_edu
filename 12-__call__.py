import math


class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        self.__counter += step
        return self.__counter


c = Counter()
c(5)
c(1)
c(3)
c(-20)
res = c(10)
print(res)


class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('Аргумент должен быть строкой')
        return args[0].strip(self.__chars)


s1 = StripChars('?:!.; ')
s2 = StripChars(' ')
res1 = s1(' Hello World! ')
res2 = s2(' Hello World! ')
print(res1)
print(res2)


class Derivate:
    def __init__(self, func):
        self.__func = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__func(x + dx) - self.__func(x)) / dx


@Derivate
def df_sin(x):
    return math.sin(x)


# df_sin = Derivate(df_sin)
print(df_sin(math.pi / 3))
