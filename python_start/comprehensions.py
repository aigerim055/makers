''' comprehensions (генераторы) '''

# a = []
# for i in range(10):
#     a.append(i)
# print(a)

# list2 = [i for i in range(10)]
# print(list2)

# comprehensions - короткий способ записи циклов для создание коллекций(словари, списки, множества, кортежи)

# list3 = [выражение for выражение in  итерируемый_обьект]

# names = ['alina', 'marina', 'vasya', 'kolya']
# quest = []
# for name in names:
#     quest.append(name + '10')
# print(quest)

# quests = [name + '10' for name in names ]
# print(quests)

# names = ['joohn', 'amina', 'mike', 'dinara', 'farida', 'aliya']

# quests = []
# for name in names:
#     if name.startswith('a'):
#         quests.append(name)
# print(quests)

# quests = [name for name in names if name.startswith('a')]
# print(quests)
# [выражениe for выражениe in итер_обьект if условие ]

# nums = [1, 2, 3, 4, 5, 6]
# new_nums = []
# for i in nums:
#     if i % 2 == 0:
#         new_nums.append(i + 0.3)
#     else:
#         new_nums.append(i + 0.6)
# print(new_nums)

# new_nums = [num + 0.3 for num in nums if num % 2 == 0 else num + 0.6] # SyntaxError

# new_nums = [num + 0.3 if num % 2 == 0 else num + 0.6 for num in nums]
# print(new_nums)
# [тернарный оператор for элемент in  итер_обьект]

# nums = [4, 3, 8, 7, 2, 1, 9]
# new_nums = []
# for i in nums:
#     if i > 5:
#         if i % 2 == 0:
#             new_nums.append(i + 0.3)
#         else:
#             new_nums.append(i + 0.6)
# print(new_nums)

# new_nums = [num + 0.3 if num % 2 != 0 else num + 0.3 for num in nums if num > 5 ]
# print(new_nums)
# 
# lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # [1, 2, 3, 4, 5 ,6 ,7 8, 9]
# new_list = []
# for i in lists:
#     print(i, 'i')
#     for j in i:
#         print(j, 'j')
#         new_list.append(j)
# print(new_list) #[1, 2, 3, 4, 5 ,6 ,7 8, 9]

# new_list = [j for i in lists for j in i ]
# print(new_list)

# a = (i for i in range(10)) # generator object
# print(a)

# a = [i for i in range(10)]
# print(a)  # [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9]

# list = [i for i in range(1,10)]
# new_list = []
# for i in range(1,10):
#     new_list.append(i)
# print(new_list)

# words = ['making', 'book', 'sitting', 'writting', 'read'], 
# list1 = [i * 2 if i.endtwith('ing') else i * 3 for i in words ]

# list_ = []
# for i in words:
#     if i.endwith('ing'):
#         list_.append(i * 2)
#     else:
#         list_.append(i * 3)
# print(list_)

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# b = {}
# for k , v in dict1.items():
#     b[k] = v
# print(b)


# c = {k:v for k,v in dict1.items()}
# print(c)