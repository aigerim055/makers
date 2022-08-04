
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

n = int(input())
dict_ = {}
for i in range(1, 501):
    if i % n == 0:
        dict_[i] = i ** 2
# print(dict_) 

dict_ = {i:i ** 2  for i in range(1, 501) if i % n == 0}
print(dict_)