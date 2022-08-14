''' области видимости и пространства имен '''
# LEGB - пространства имен
# Local -локальная
# Enclosed - замкнутая
# Global - глобальная
# Built-in -  встроенная

# область видимости - часть программы, где будет доступно то или иное имя(переменная, функция, класс и т.д)

# name = 'Janat'
# name = 'Akbar'

# print(name) # Akbar

# name = 'Marina' # global

# def func():
#     name = 'Vasya'
#     print(name)
# print(name) # Marina
# func() # Vasya

# def func():
#     # local
#     print(name)
# func() # Marina


# def func3():
#     a = 10
# print(a) # NameError

# имена из локальной области недоступны в глобальной области, но в локальной области доступны имена из глобальной области


# for i in range(1, 10):
#     res = 1 * 2
# print(res)

# num = 20
# if num % 2 != 0:
#     res2 = 35
# print(res2)

# num = 10
# def func():
#     global num
#     num = 50

# func()
# print(num) # 50


# x = 20 # global
# def func_outer():
#     x = 15 # nonlocal
#     def func_inner():
#         x = 25 # local
#         print(x)
#     func_inner()
# func_outer() # 25


# number = 20
# def outer_func():
#     # nonlocal
#     number = 19
#     print(number)# 19
#     def inner_func():
#         nonlocal number
#         number = 25
#         print(number) #25
#     inner_func()
#     print(number) # 25
# outer_func() 

''' globals(), locals() '''
# a = 20
# print(globals())
# globals() - показывает имена на глобальном уровне видимости

# print(locals())
# def my_func():
#     var = 95
#     tel = 100
#     print(locals())
# my_func()
#   locals() - показывает именя той области, в которой была вызвана


# def get_grage(mark):
#     mark = 1
#     grade = 0
#     if mark > 87:
#         grade = 5
#     return grade
# get_grage(85)

# 
# def func(a, b, c):
#     return a + b + c
# nums = (3, 4, 8)
# print(func(*nums))

