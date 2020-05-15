import pickle

name ='name.data'
name1 =['Павел', 'Илья', 'Егор', 'Кирил']
f = open(name, 'wb')
pickle.dump(name1, f)
f.close()

del name1

f = open(name, 'rb')
n = pickle.load(f)
print(n)

