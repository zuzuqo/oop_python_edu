class Goods:
    def __init__(self, name: str, weight: float, price: float):
        # через super, чтобы у дочернего класса сработал init другого наследуемого класса
        super().__init__()
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name} - {self.weight} кг. - ${self.price}')


class MixinLog:
    ID = 0

    def __init__(self):
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f'ID {self.id}: товар был продан')

    def print_info(self):
        print('MixinLog - print_info')


class NoteBook(Goods, MixinLog):
    def print_info(self):
        MixinLog.print_info(self)


n = NoteBook('ROG Flow X13', 1.3, 1400)
l = NoteBook('Lenovo ThinkBook', 1.5, 400)
n.print_info()
n.save_sell_log()

print(NoteBook.__mro__)

l.print_info()
