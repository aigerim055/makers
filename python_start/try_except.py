''' try except '''

# try except - контрсукция для обработки исключений 

'''исключение - прооблема в логике работы кода'''

# ZeroDivisionError - ошибка деления на ноль
# print(10 / 0)

# NameError - исключение отсутствия имени
# a = 10
# b = 20
# print(c)

# AttributeError - ошибка атрибута 
# string = 'word'
# string.get('o')

# KeyError - ошибка ключа
# dict_ = {'a': 10, 'b': 20}
# dict_['c']

# IndexError - индекс не входит в диапазон списка
# list_ = [1, 2, 3]
# list_[4]

# TypeError - ошибка типов, когда тип обьектане подходит к операции
# string = 'youtube'
# num1 = 12
# string  + num1

# ValueError - ошибка значения, когда тип обьекта подходит для операции, но значение - нет
# int(12)    #OK
# int(12.5)  #OK
# int('103') #OK
# print(int('hello')) # ValueError
# from math import sqrt
# print(sqrt(25)) #OK
# print(sqrt(-20))# ValueError



# import wrong_module #ModuleNotFoundError
# from math import wrong_module #ImportError



'''ошибка - проблема в синтаксисе кода. Например: скобки, двоеточия, отступа и т.д'''

# SyntaxError 
# for i in range(1, 10)
#     print(i)

# IndentationError -  ошибка отступа
# for i in range(1, 10):
# print(i)

# TabError -  ошибка табуляции(смешивание пробелов и табуляций)
# for i in range(1, 10):
#       print(i)



# print('hello')
# print(10 / 0)
# print('world')



# try:
#     print('hello')
#     print(10 / 0)
#     print('world')
# except:
#     print('что то поошло не так!')
# else:
#     print('try обработал без ошибок')
# finally:
#     print('я отработаю в любом случае')


# try:
#     попыптка выпольнить код, которая потенционально может вызвать исключение 
# except:
#     обработка исключений - сработает, если в try есть исключение
# else:
#     выподняется, если try прошел без исключений
# finally:
#     выполняется в любом случае



# try:
#     print(c)
# except Exception as e:
#     print(e)

# print('drugoi uchastok koda')
# 10 + 10


# dict_ = {'a':10, 'b': 20}
# try:
#     print(10 / 0)
#     print(dict_['d'])
# except KeyError:
#     print(' нет такого ключа ')
# except ZeroDivisionError:
#     print('на ноль делить нельзя')

# a.get('d', 'нет такого ключа')

# print('drugoi uchastok koda')


# a = [1, 2, 3 ]
# try: 
#     print(a[10])
#     print(b.get('3'))
# except (IndexError, AttributeError):
#     print('нет такого индекса или нет такого метода')


# raise - оператор генерации собствнных исключений
# raise название_искл(описание исключения)

# temp = int(input('vvedite temperaturu: '))
# if temp > 100:
#     raise ValueError('температура не может быть выше 100 градусов')
# print('еще какой нибудь код')


# num1 = 10
# num2 = 0
# try:
#     num1 / num2
# except ZeroDivisionError:
#     print('na 0 delit nelxya')

# if num2 != 0:
#     num1 / num2
# else:
#     print('na 0 delit nelxya')

# try:
#     for i in range(10)
#         print(i)
# except SyntaxError: нельзя обработать так как ошибка в самом коде
#     print('ne pravilno')


