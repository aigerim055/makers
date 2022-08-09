''' функции  '''

# print()
# max()
# pow()

# функия - это именованный блок кода, который принимает каиее-то значения,
# совершает над ними определенные действия и возвращает результат этих действий.

# a1 = 100
# (a1 ** 2) / 10 * 15
# a2 = 200
# (a2 ** 2) / 10 * 15

# DRY(dont repeat yourself) - не повторяйся

# def func():
#     print('hello world')
# func()

# def my_sqr(num):
#     print((num ** 2) / 10 * 15)

# a = my_sqr(100) # None
# a + 500 #TypeError
# my_sqr(200)


# def my_func(num):
#     return (num ** 2) / 10 * 15
# b = my_func(100)
# print(b)         #15000.0
# print(b + 5000)  #20000.0

# a = print()
# print(a)

# def func():
#     return None

# def имя_функции(параметры):
    # тело функции

# имя_функции(аргумент)
# параметры - это значения функции при обьявлении 
# аргументы - это значения для функции при вызове

# return - это ключевое слово для возвращения результата выполнения функции


# def add(x: int, y: int) -> int:
#     ''' принимает 2 числа и складывает их между собой ''' # строка докумаентации(doctstring)
#     num = x + y
#     return  num

# a = add(2, 2)
# print(a)


# #  параметры бывают 2 типов: 
# 1. обязательными (с)
# 2. необязательными(по умолчанию) (с=10)


# def sub(x, y):
#     result = x - y
#     return result

# a = sub(25, 10) # 15
# print(a)

# def sub1(x, y=5):
#     result = x - y
#     return result

# b = sub1(10) # 5
# c = sub1(30, 10) # 20
# print(c)
# print(b)

# def func(x=5, y): #SyntaxError - обязательные параметры нужно указывать первыми

# def func(a, b, c, d, e=10, f=20):
    # pass


# аргументы бывают 2 типов:
# 1. именованные
# 2. позиционные

# def my_func(num1, num2, num3=10):
    # return num1 + num2 + num3

# позиционные
# my_func(10, 10, 20) # 40
# my_func(50, 60) #120

# именованные
# my_func(num1=5, num2=10, num3=15) # 30
# my_func(num3=10, num1=5, num2=7)  # 22
# my_func(10, 5, num3=10) # 25
# my_func(num3=5, 5, 10) # Error
# my_func(10, 5, num1=15) #Error

# def send_massage(email, massage):
#     return f'{massage} было отправлено на {email}'

# def notify_user(name):
#     massage = input('your massage: ')
#     email = input('your email: ')
#     note = send_massage(email, massage )
#     print(f'hello {name}. {note}')

# notify_user('aktan')

# print(1, 2, 3,45,6)
# print()

# *args - кортеж позиционных аргументов (arguments)
# **kwargs - словарь именованных аргументов (keyword arguments)

# def func(*args, **kwargs):
#     print(args, 'args')
#     print(kwargs, 'kwargs')

# func(1, 2 ,3) # args -> (1, 2, 3)
# func(a=1, b=3, v=99) # kwrags -> {'a':1, 'b':3, 'v':99}
# func(1, 2, 3, a=1, b=2, c=3)



# def my_func(*args):
#     counter = 0
#     for i in args:
#         counter += i
#     return counter
# print(my_func(1, 2, 3, 4, 'hello', 6))