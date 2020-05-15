# 'ab' - сокращение от 'a'ddress'b'ook

ab = {  'Swaroop'    : 'swaroop@swaroopch.com',
        'Larry'      : 'larry@wall.org',
        'Matsumoto'  : 'matz@ruby-lang.org',
        'Spammer'    : 'spammer@hotmail.com'
     }
print("Адрес Swaroop'а:", ab['Swaroop'])

# Удаление пары ключ-значение
del ab['Spammer']
print('\nВ адресной книге {0} контактов\n'.format(len(ab))) # НАШЛО 3 КОНТАКТА ТАК КАК МЫ УКАЗАЛИ .FORMAT
for name, address in ab.items(): #аб айтемс это айтемы строки
    print('Контакт {0} с адресом {1}'.format(name, address)) # так как мы вбили строку с лари и вывели от 0 до 1
    # можно было только напечатать лари

# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print(''
          'Адрес Guido:', ab['Guido']) #/n это табуляция !!!

