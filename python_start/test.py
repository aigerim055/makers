
#task24
# string1 = "America" 
# string2 = "Japan" #"AJrpan"
# print(f'{string1[0]}{string2[0]}{string1[3]}{string2[2:]}')




#task11
# string = 'hello'
# print(string[-1::1])

# task9
# year = int(input())
# if year / 400:
#     print('yes')
# else:
    # print('no')

# string = 'hello' #oellH

# print(f'{string[-1]}{string[1:-1]}{string[0]}')

# nums = [1, 15, 36, 88]
# target = 0
# if target in nums:
#     print('yes')
# else:
#     print('no')



# name_of_list = ['helloworld!']
# string = name_of_list[0]
# half_of_string = len(string) // 2 + 1
# if not len(string) % 2 == 0:
#     new_list = list(string[half_of_string:] + string[0:half_of_string])
# else:
#     new_list = list(string[half_of_string+ 1:] + string[0:half_of_string+ 1])
# print(new_list)


'''Создать три числа в списке list_.
Вывести на экран yes, если среди них есть одинаковые, иначе вывести ERROR.
Например, для списка [1, 1, 3], вывод будет:

yes 
а для списка [1, 2, 3]:

'''

# list_ = [5, 6, 44]
# TASK 14
# counter1 = list_.count(list_[0])
# counter2 = list_.count(list_[1])

# if counter1 == 2 or counter2 or counter1 == 3:
#     print('yes')
# else:
#     print('ERROR')


# list1 = [1, 2, 3, 3, 5, 6, 7,3]
# list2 = [8, 9, 12, 1, 3, 4, 5]
# res = []
# #[1, 3 ,5]

# # for i in list1:
# #     for j in list2:
# #         if i == j:
# #             res.append(i)
# # print(res)
# i = 0
# j = 0

# while i != len(list1):
#     while j != len(list2):
#         if list1[i] == list2[j]:


# list1 = ['world','hello']

# new_list = list1[::-1]
# print(new_list)

# a = {'a': 1, 'b': 2, 'c': 1} 

# for k , v in a.items():
#     print(k,v)

# list_ = []
# for num in range(1,50):
#     if num % 2 != 0:
#         list_.append(num)
# print(list_)

# list1 = [num for num in range(1, 50) if num % 2 != 0]
# print(list1)

# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list1  = []
# for num in list_:
#     if num > 0:
#         if num % 2 == 0:
#             int_list1.append(num)
# print(int_list1)


# int_list = [num  for num in list_ if num > 0 if num % 2 == 0]
# print(int_list)

# list1 = []
# for i in range(1, 26):
#     list1.append(i ** 2)
# print(list1)

# list_ = [ i ** 2 for i in range(1, 26)]
# print(list_)

# list1 = []
# for i in range(1, 101):
#     if i % 2 == 0:
#         list1.append(i ** 2)
#     else:
#         list1.append(i)
# print(list1)

# list_ = [i ** 2 if i % 2 == 0 else i for i in range(1,101) ]
# print(list_)

# list1 = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         list1.append(True)
#     else:
#         list1.append(False)
# print(list1)

# list_ = [True if i % 2 == 0 else False for i in range(1, 11)]
# print(list_)

# list_name1 = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list1 = []
# for name in list_name1:
#     if len(name) <= 4:
#         new_list1.append('shorter')
#     else:
#         new_list1.append('longer')
# print(new_list1)

# new_list = ['shorter' if len(name) <= 4 else 'longer' for name in list_name1]
# print(new_list)

# dict_ = {}
# for i in range(1,10):
#     dict_[i] = i ** 2
# print(dict_)

# dict_ = {i: i **2 for i in range(1, 10) }
# print(dict_)

# n = int(input())
# dict_ = {}
# for i in range(1, 501):
#     if i % n == 0:
#         dict_[i] = i ** 2
# # print(dict_) 

# dict_ = {i:i ** 2  for i in range(1, 501) if i % n == 0}
# print(dict_)

# list_ = []
# for num in range(11):
#     if num % 2 == 0:
#         print(num)
#         list_.append(num // 2)
# print(list_)

# list1 = [num // 2 for num in range(11)  if num % 2 == 0 ]
# print(list1)


# TASK 17
# dict1 = {1:'hello', 2: 'fucking', 3: 'world', 4: '!'}
# for k,v in dict1.items():
#     if k % 2 == 0:
#         dict1[k] = len(v)
#     else:
#         dict1[k] = len(v) ** 3
# print(dict1)

# a = {k: len(v) if k % 2 == 0 else len(v) ** 3 for k,v in dict1.items()   }
# print(a)



# TASK12
# dict_ = {'first': 1, 'second': 2, 'third': 3}
# # for k,v in dict_.items():
# #     if v % 2 == 0:
# #         dict_[k] = 'even'
# #     else:
# #         dict_[k] = 'odd'
# # print(dict_)
# a = {k: 'even' if v % 2 == 0 else  'odd' for k,v in dict_.items() }
# print(a)



# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = []
# for i in str_list:
#     int_list.append(int(i))
# print(int_list)

# int_list = [int(i) for i in str_list ]
# print(int_list)

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = []

# # string_.split()
# for strr in string_.split():
#     if strr.isalnum:
#         list_.append(strr)
# # if string_.split().isalnum():
# #     list_.append(string_)

# print(list_)

# TASK18
# set1 = {n for n in range(10)}
# set2 = {n for n in range(10,20)}
# full_set = set1.union(set1 , set2)
# if len(full_set) < 20:
#     print(f"В этом сете было {20 - len(full_set)} повторения, его длина составляет {len(full_set)}")
# else:
#     print("Ваш обьединенный сет полностью уникальный!")

# # TASK11
# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = 


# dict_ = {'key1': 'value1', 'key2': 'value2'}
# try:
#     print(dict_['key3'])
# except KeyError:
#     print('Нет такого ключа!')



# def get_string_length(string):
#     return len(string)
# print(get_string_length('hello'))


# def get_type(type1, type2):
#     print(type(type1))
#     print(type(type2))
#     return
# get_type(5, 'hello')


# def divide(x, y):
#     return x / y
# print(divide(10, 5))



# dict_ ={}
# def dictionary({'a':3, 123:3}):
#     for i in dict_.items():
#         print(i)
#     return
# dictionary()

num = 6
def check(num):
    if num %2 == 0:
        "It is even number"
    else:
        "It is odd number"
    

print(check(num))