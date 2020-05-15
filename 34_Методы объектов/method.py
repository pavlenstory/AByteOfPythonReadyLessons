class Person:
    def sayHi(self):
        print('Привет как твои дела?')

p = Person() # программа сначала берет Person. и внутри Person содержиться SayHI
p.sayHi()
# Этот короткий пример можно также записать как Person().sayHi()