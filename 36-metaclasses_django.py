class Meta(type):
    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name, bases, attrs):
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs


class Women1(metaclass=Meta):
    title = 'заголовок'
    content = 'контент'
    photo = 'путь к фото'

# класс Women2 аналогичен классу Women1, но Women1 создается с помощью метакласса Meta, а Women2 необходим инициализатор
class Women2:
    class_attrs = {'title': 'заголовок', 'content': 'контент', 'photo': 'путь к фото'}
    title = 'заголовок'
    content = 'контент'
    photo = 'путь к фото'

    def __init__(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value


w1 = Women1()
print(f'Women1 - {w1.__dict__}')

w2 = Women2()
print(f'Women2 - {w2.__dict__}')
