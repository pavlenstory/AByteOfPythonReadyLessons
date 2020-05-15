class ShortInputException(Exception):
    '''Пользовательский класс исключения.'''
    def __init__(self, length, atleast): #длина, не менее
        Exception.__init__(self)
        self.length = length
        self.atleats = atleast

try:
    text = input('Введите что-нибудь --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
# Здесь может происходить обычная работа
except EOFError:
    print('Ну зачем вы сделали мне EOF?')
except ShortInputException as ex: #В пункте except мы указываем класс ошибки ShortInputException,
# который будет сохранён как3 переменная ex
    print('ShortInputException: Длина введённой строки -- {0}; \
        ожидалось, как минимум, {1}'.format(ex.length, ex.atleast))
else:
    print('Не было исключений.')









