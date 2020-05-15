shoplist = ['Яблоко', 'морковь', 'огурец', 'дыня'] #список покупок
print('я должен купть', len(shoplist),'продукта') #лен выводит строку шоп листа

print('Покупки:', end=' ') #end мы привсвоили слово шоп лист
for item in shoplist:
    print(item, end=' ')

print('\nТакже нужно купить риса.') #с помощью /n мы добавили shoplist.append('рис'). И теперь появился рис
shoplist.append('рис')
print('Теперь мой список покупок таков:', shoplist)

print('Отсортирую-ка я свой список')# отсортировали список с помощью shoplist.sort()
shoplist.sort()
print('Отсортированный список покупок выглядит так:', shoplist)

print('Первое, что мне нужно купить, это', shoplist[0]) #список начинаеться  нуля
olditem = shoplist[0] #присвоили Яблоку имя olditem
del shoplist[0]
print('Я купил', olditem)
print('Теперь мой список покупок:', shoplist)