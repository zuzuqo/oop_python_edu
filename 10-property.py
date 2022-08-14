from string import ascii_letters


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, age, passport, weight):
        self.fio = fio
        self.age = age
        self.passport = passport
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой')
        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат записи')

        # разрешенные символы
        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должен быть хотя бы один символ")
            if len(s.strip(letters)) != 0:
                raise TypeError('В ФИО можно использовать только буквенные символы и дефис')

    @classmethod
    def verify_age(cls, age):
        if type(age) != int or age < 14 or age > 120:
            raise TypeError('Возраст должен быть целым числом в диапазоне [14; 120]')

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) not in (float, int) or weight < 20:
            raise TypeError('Вес должен быть числом от 20 и выше')

    @classmethod
    def verify_passport(cls, passport):
        if type(passport) != str:
            raise TypeError('Паспорт должен быть строкой')
        s = passport.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('Неверный формат паспорта')

        for p in s:
            if not p.isdigit():
                raise TypeError('Неверный формат паспорта')

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.verify_passport(passport)
        self.__passport = passport


p = Person('Иванов Иван Иванович', 30, '9940 567890', 75)

print(p.__dict__)
