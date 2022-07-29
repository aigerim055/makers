''' списки и циклы '''

# list()
# список - это изменяемый, упорядоченный, индексируемый, итерируемый тип данных.Нужен для хранения нескольких элементов.

# элементами списка могут быть любыe типы данных

# list_ = [1 , 'str' , True , False , [2,3] , None , {'a': 12} , {1, 2} , ('a' , 'b' , 'c')]
# print(list_)






list1 = [1, 2, 3, 4, 5, [6, 7]]
        #0   1  2  3  4    5
list1[0] #1
list1[1] #2
list1[2] #3
list1[5] #[6, 7]
list1[5][0] #6
list1[-1] #[6, 7]

list1[1:-2:] #[2, 3, 4]

''' методы добавление элементов в список'''

# a = [1, 2, 3]

# a.append(element) - добавляет переданный элемент в конец списка
# print('do', a)
# a.append(4)
# a.append(5)
# print('posle', a)

# a.insert(index, element) - вставляет элемент на место указанного индекса
# print('do', a)
# a.insert(1, 'hello')
# print('posle', a)

# a.append(element) -> a.insert(len(a), element)

# a.insert(1234, 'world') # добавит в конец [1, 2, 3, 'world']

# list1.extend(list2) - добавляет все элементы list2 в list1

# my_list1 = [4, 2, 6]
# my_list2 = [1, 3, 8]

# my_list1.append(my_list2)
# print(my_list1) # [4, 2, 6, [1, 3, 8]]

# my_list1.extend(my_list2) 
# print(my_list1) # [4, 2, 6, 1, 3, 8]

# a = my_list1 + my_list2
# print(my_list1) #[4, 2, 6]
# print(a) #[4, 2, 6, 1, 3, 8]


''' замена элементов '''
# b = ['a', 'b', 'c', 'd']
# b[2] #'c'
# b[2] = 'g'
# print(b) # ['a', 'b', 'g', 'd']

''' удаление элементов'''
ab = ['a', 'b', 'c', 'd']

# ab.pop([index]) - удаляет элемент по указанному индексу, но если индекс не указан - удаляет последний элемент. ->
# -> Возвращает удаленный элемент.

# ab.pop(1)
# print(ab) # ['a', 'c', 'd']

# ab.pop()
# print(ab) #['a', 'b', 'c']

# deleted_el = ab.pop(2)
# print(deleted_el) # c
# print(ab) # ['a', 'b', 'd']
# ab.append(deleted_el) # ['a', 'b', 'b', 'c']

# list3.remove(значение) - удаляет первый встретившийся элемент с указанным значение

# list3 = ['azamat', 'kolya', 'adilet', 'azamat']
# list3.remove('azamat')
# print(list3) # ['kolya', 'adilet', 'azamat']
# list3.remove(20) #ValueError

#ab.clear() - полностью очищает список
# ab.clear()
# print(ab) #[]

# # del element 
# del ab
# print(ab)

# del ab[1]
# print(ab) # ['a', c' , 'd']

# del ab[:2]
# print(ab) # ['c', 'd']

# a1 = [1, 2, 3]
# b2 = a1
# b2.append(4)
# print(b2) #[1, 2, 3, 4]
# print(a1) #[1, 2, 3, 4]
# print(b2 is a1) # True


''' копирование списка '''
# a3 = [1, 2, 3]
# a4 = a3.copy()
# a5 = a3[:]


''' сортировка списка '''

num_list = [4, 3, 8, 5]
# num_list.sort()
# print(num_list) #[3, 4, 5, 8]

# num_list.sort(reverse=True) - сортировка в обратном порядке
# print(num_list) #[8, 5, 4, 3]

# str_list = ['b', 'c', 'e', 'a', 'd']
# str_list.sort()
# print(str_list) # ['a', 'b', 'c', 'd', 'e']

name_list = ['azamat', 'ivan', 'zeynep', 'aliya']
# name_list.sort(key=len)
# print(name_list) #['ivan', 'aliya', 'azamat', 'zeynep']
# name_list.sort(reverse=True)
# print(name_list) # ['zeynep', 'ivan', 'azamat', 'aliya']

# new_namelist = sorted(name_list, key=len, reverse=True)
# print(name_list) #['azamat', 'ivan', 'zeynep', 'aliya']
# print(new_namelist) # ['azamat', 'zeynep', 'aliya', 'ivan']

# my_list = ['a', 'b', 'c', 'd', 'e']
# my_list.reverse()
# # print(my_list) #['e', 'd', 'c', 'b', 'a']


b5 = ['a', 'b', 'c', 'a', 'a']
# print(b5.count('a')) # 3

# print(b5.index('c')) # 2

''' циклы '''

# цикл - многократное выполнение определенного участка кода


iter_list = [1, 2, 3, 4, 5]
# iter_list[0]
# iter_list[1]
# iter_list[2]
# iter_list[3]
# iter_list[4]



# 1. for
# 2. while

# for item in iter_list:
        # print(item)
        

# итерация - это повторения какого либо действия

# for - цикл работает до тех пор, пока элементы в итерируемом обьекте не заканчиваются
# for елемент in итерируемый_обьект:
# #         тело цикла

# mail_list = ['azamat', 'mirbek', 'baatai', 'alym']
# result = []
# for  name in mail_list:
#         gmail = name  + '@gmail.com'
#         result.append(gmail)
# print(result)


# int 
# list
# str
# bool
# set
# None
# dict
# tuple

# # print(dir(list))

# types_list = [int, str, list, bool, None, dict, set, tuple]
# iter_objs = []
# non_iter_objs = []

# for obj in types_list:
#         if '__iter__' in dir(obj):
#                 iter_objs.append(obj)
#         else:
#                 non_iter_objs.append(obj)
# print(f'iter obj: \n{iter_objs}')
# print(f'non iter obj: \n{non_iter_objs}')

# range() - функция для генерации последовательности чисел
# range(start, stop, step)
# range(stop)
# print(list(range(10))) #преобразование последовательности чисел в список из чисел

# num_list = []
# for num in range(9,101):
        # num_list.append(num)
# print(num_list)

# num_list = []
# for num in range(1,101):
#         if num % 2 == 0:
#                 num_list.append(num)
# print(num_list)

# for num in range(0, 101, 2):
#         num_list.append(num)
# print(num_list)

# list_lists = [[1, 2, 3], ['a', 'b', 'c'], [4, 5, 6]]
# for list1 in list_lists:
#         for elem in list1:
#                 print(elem)

# for _ in range(5):
#         print('hello')


''' цикл while '''
# num = 10
# while num < 11:
#         print(num)
# Бесконечный цикл
# while True:
        # print('hello')

# while условие - цикл работает до тех пор, пока условие истинно(True)

# msg = input('vvedite soobshenie ili stop: ')
# while msg != 'stop':
#         print(msg)
#         msg = input('vvedite soobshenie ili stop: ')

# break - останавливает работу цикла
# continue - пропускает работу цикла

# while True:
        # msg = input('vvedite soobshenie ili stop: ')
        # if msg == 'stop':
        #         print('-- STOP --')
        #         break
        # print(msg)

# while True:
#        msg = input('vvedite soobshenie: ')
#         if msg == 'bue':
#                 print('-- BYE --')
#                 continue
#         print(msg)

# for num in range(10):
#         print(num)
# else:
#         print('-- STOP --')

# else в циклах срабатывает при успешном окончании цикла

# for num in range(10):
#         if num == 5:
#                 break
# else:
#         print('-- STOP --')



