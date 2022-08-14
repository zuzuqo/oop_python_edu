class ExceptionPrint(Exception):
    '''
    Общий класс исключения принтера
    '''


class ExceptionPrintSendData(ExceptionPrint):
    '''
    Класс исключений при отправке данных принтеру
    '''

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f'Ошибка: {self.message}'


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f'печать: {str(data)}')

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData('Принтер не отвечает')

    def send_to_print(self, data):
        return False


p = PrintData()
# p.print('123')

try:
    p.print('123')
except ExceptionPrintSendData:
    print('Принтер не отвечает')
except ExceptionPrint:
    print('Общая ошибка печати')