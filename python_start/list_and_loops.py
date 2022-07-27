''' списки и циклы '''

# list()
# список - это изменяемый, упорядоченный, индексируемый, итерируемый тип данных.Нужен для хранения нескольких элементов.

# элементами списка могут быть любыe типы данных

# list_ = [1 , 'str' , True , False , [2,3] , None , {'a': 12} , {1, 2} , ('a' , 'b' , 'c')]
# print(list_)

import numbers
from re import S


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
# ab.appen(deleted_el) # ['a', 'b', 'b', 'c']

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


