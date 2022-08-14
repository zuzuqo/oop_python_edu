class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1,
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


th1 = ThreadData()
th2 = ThreadData()

print(th1.id, th1.name)
print(th2.id, th1.name)

th1.name = 'new_name'
th2. id = 200

print(th1.id, th1.name)
print(th2.id, th1.name)

th1.new_attr = 'this is new attr!'

print(f'\nth1: {th1.__dict__}')
print(f'\nth2: {th2.__dict__}')
