''' кортеж(tuple) '''

# кортеж - неизменяемая последовательность элементов. Ведет себя как список, но не изменяется.

# print(dir(tuple))

# my_tuple = (1, 2, 3, 4, 5)
# print(type(my_tuple)) # tuple
# a = (2)
# print(type(a)) # int
# b = ('str',)
# print(type(b)) # tuple
# c = [1, 2, 3, 4], 'string', 3
# print(type(c)) # tuple
# d = 1,
# print(type(d)) # tuple


# tuple1 = (1, 1, 3, 4, 5, 1)
# print(tuple1.count(1))  # 3
# print(tuple1.index(4))  # 3

# num1 = 1
# num2 = 2
# num3, num4 = 4 , 7
# print(num3 , num4) # 4 7

# tuple2 = ('str2', 'str2', 'str3')
# print(*tuple2)                          # str2 str2 str3
# print(tuple2[0], tuple2[1], tuple2[2])  # str2 str2 str3

# nums = (10, 5)
# print(pow(*nums)) # 10**5 --> 100000

# a, b, *c = 1, 2, 3, 4
# print(a)  # 1
# print(b)  # 2
# print(c)  # [3, 4]

# a = (1, 2 ,3 ['str', 'str2'])
# # a[2] = 5  # TypeError
# a[3].append(4)
# print(a) 


# new_tuple = (('name', 'Alina'), ('name', 'Marina'), ('name', 'Kayrat'), ('name', 'Mirbek'))

# for i in new_tuple:
    # print(i)

# for key, value in new_tuple:
#     print(f'{key}: {value}')


# list_ = [1, 2 , 3, 4, 5]
# for i in list_: 
#     print(i)

# index = 0 
# while index < len(list_):
#     print(list_[index])
#     index += 1

# index = index + 1 <--> index += 1

'''# Написать программу, которая будет запрашивать количество денег, которое Вы хотите потратить. 
Если указанное число больше чем денег в кошельке - программа предупреждает об этом и останавливается
. Иначе отнимает указанное число из кошелька и печатает количество оставшихся денег'''

# money = 10000
# m = int(input('skol\'ko deneg vy xotite potratit\'? '))
# while True:
#     if m > money:
#         print('у вас  не достаточно денег')
#         break
#     elif m < money:
#         ostatok = money - m
#         print(f'у вас осталось {ostatok}')
#         msg = input('хотите продолжить? да\нет: ')
#         if msg == 'да': 
#              m = int(input('skol\'ko deneg vy xotite potratit\'? '))
#         else:
#             print('goodbye')
#             break
    
# while True:
#     x = int(input('sk xotite potratit? '))
#     if money < x:
#         print('no money')
#         break
#     money -= x
#     print(f'ostatok{money}')


# len(последовательность) - возвращает количесмтво элементов в последовательности
# max(последовательность)
# min(последовательность)
# sum(последовательность)

# numbers = (2, 6, 1, 4, 5)
# print(max(numbers)) # наибольшее число
# print(min(numbers)) # наименьшее число
# print(sum(numbers)) # суммирует все числа

# counter = 0
# for num in numbers:
#     counter += num
# print(counter)


# tuple3 = (1, 2, 3)
# tuple3 = list(tuple3)

# a = [1, 2, 3]
# b =(1, 2, 3)
# print(a.__sizeof__())
# print(b.__sizeof__())

# peremennaya.__sizeof__() - можно увидеть сколько памяти занимает

