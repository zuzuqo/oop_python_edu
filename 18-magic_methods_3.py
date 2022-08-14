class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if item <= len(self.marks):
            return self.marks[item]
        else:
            raise IndexError('Неверный индекс')

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError('Индекс должен быть целым числом')

        # если вызываемый индекс больше длины списка, то список расширяется элементами None
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)

        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('Индекс должен быть целым числом')

        del self.marks[key]




s1 = Student('Rick', [5, 5, 3, 2, 5])
s1[3] = 4
print(s1.marks)
