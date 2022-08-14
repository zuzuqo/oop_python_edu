class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        print('NEW ' + f'{cls}')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'connecting to DB: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('close connection with DB')

    def read(self):
        return 'data from DB'

    def write(self, data):
        print(f'write data into DB: {data}')


db = DataBase('admin', '12345', 8000)
db2 = DataBase('dadada', '12345q', 6000)

print(db, db2)
db.connect()
db2.connect()
