class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age


p = Person('Mark', 20)
print(p.__dict__)

p.__dict__['age'] = 'age in object p'
print(p.__dict__)

print(p.age)

p.age = 29
p.name = 'StAss'
print(p.__dict__)

p2 = Person('Niko', 34)
del p2.age
print(p2.__dict__)
p2.age = 35
print(p2.__dict__)
