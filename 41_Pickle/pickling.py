import pickle

#имя файла, в котором мы сохраним обьект
shoplistfile = 'shoplist.data'
# список покупок
shoplist = ['яблоки', 'манго', 'морковь']

# Запись в файл

f = open(shoplistfile, 'wb')#режим биннарной оозаписи b
pickle.dump(shoplist, f) # помещаем объект в файл
f.close()

del shoplist # уничтожаем переменную shoplist

# Считываем из хранилища
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) # загружаем объект из файла
print(storedlist)





