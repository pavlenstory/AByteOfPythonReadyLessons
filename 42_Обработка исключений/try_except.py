try:
    text = input('Введите что-нибудь:')# Сама программа помещаетьтся в тру блок
except EOFError: #оброботчики исключений в except
    print('Ну и зачем вы сделали мне EOF?')
except KeyboardInterrupt:
    print('Вы отменили операцию.')
else:
    print('Вы ввели {0}'.format(text))



