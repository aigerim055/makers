""" Множества (set) """
# Множества - изменяемый, неупорядоченный тип данных. Содержит в себе уникальные элементы и только неизменяемые типы данных.

# a = {}
# print(type(a)) # dict

# b = set()
# print(type(b)) # set

# c = {'a', 3, True, False, 0, (1, 2), 2.54, None}
# print(c) # Ok

# d = {1, 1, 1, 1}
# print(d) # {1}
# print(len(d)) # 1


# e = {1, 2, ['a', 'b']} # TypeError

# d = {1, 2, (1, 2, ['b', 'c'])} # TypeError

# list_ = [1, 2, 4, 4, 4, 3, 1]
# a = list(set(list_))
# print(a)

# from string import ascii_lowercase
# print(ascii_lowercase)

# from string import ascii_lowercase
# 'abcdefghijklmnopqrstuvwxyz'
# a = {}
# num = 1
# for i in ascii_lowercase:
#     a[i] = num
#     num += 1

# print(a)
# {'a': 1, 'b': 2.....}

# print(ord('a'))
# print(chr(97))
# 26
# {'a': 1, 'b': 2.....}


# string = 'pythondor'
# dict_ = {}
# for i in string:
#     num = ord(i)-96
#     dict_.setdefault(i,num)
# print(dict_)
#ord() a = 97 - 96 = 1
# alph = []
# for i in range(97, 123):
#     alph.append(chr(i))
# print(alph)
# dict_ = {}
# for i in alph:
#     dict_[i] = ord(i) - 96
# print(dict_)


# alph = {}
# for i in range(97, 123):
#     alph.setdefault(chr(i), i - 96)
# print(alph)

# a = {}
# for i in range(26):
#     a[chr(i + ord('a'))] = i + 1
# print(a)

# emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
#       	'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
#       	'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
#       	'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
#       	'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
#       	'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

# for k, v in emails.items():
#     # print(k)
#     # print(v)
#     for name in v:
#         print(name + '@' + k)