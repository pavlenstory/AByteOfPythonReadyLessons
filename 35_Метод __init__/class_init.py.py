class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print('Привет меня завут', self.name)
p = Person('Павел')
p.sayHi()
# Этот короткий пример можно также записать как Person('Павел').sayHi()