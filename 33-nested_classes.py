class Women:
    title = 'Women - title'
    photo = 'Women - photo'
    ordering = 'Women - ordering'

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(user + '@' + psw)  # чтобы создать объект вложенного класса Meta

    class Meta:
        ordering = ['Meta - id']

        # t = Women.title                           тут еще нельзя обращаться к классу родителю, поскольку он еще не создан

        def __init__(self, access):
            self.access = access
            # self._t = Women.title                   # а в инициализаторе можно, но лучше не надо. внутренний класс должен использоваться внешним, а не наоборот


w = Women('root', '1234')
print(w.ordering)
print(w.Meta.ordering)
print(w.__dict__)
print(w.meta.__dict__)
