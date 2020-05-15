#Указание отрицательного шага,
# т.е. -1 приведёт к выводу текста
#в обратном порядке(:-1) ЧИТАЕТ ТЕКСТ В ОБРАТНО ПОРЯДКЕ

def reverse(text):
    return text[::-1]
def is_palindrome(text):
    return text != reverse(text) # != это обозночает не равен
something = input('Введите текст: ')
if is_palindrome(something):
    print("Нет, это не палиндром")
else:
    print("Да, это палиндром")

