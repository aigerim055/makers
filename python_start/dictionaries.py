''' словари (dict) '''

'''словарь - изменяемый, итерируемый. Состоят из пар: ключ: значение. Ключи могут быть только неизменяемые
    типы данных(tuple, str, int,None, bool), а значениями - любые. Ключи должны быть уникальными'''

# dict_ = {}

passport = {'name': 'aigerim', 'last_name': 'suyumbaeva', 'age': 17, 'gender': 'j', 'birthday' : '08.08.2005'}
# passport['name']   # 'aigerim'
# passport['age']    #  17
# # print(passport[0]) # KeyError

# dict2 = dict(name='aigerim', last_name='ssss', age=17, gender='J')
# # print(dict2) 

# dict3 = dict.fromkeys(['a', 'b'], 25)
# print(dict3) # {'a': 25, 'b': 25} 


# dict4 = dict.fromkeys(['a', 'b'])
# print(dict4) # {'a': None, 'b': None} 

# dict5 = dict([('name', 'vasya'), ('last_name', 'pupkin')])
# print(dict5)

''' методы словарей '''

passport = {'name': 'aigerim', 'last_name': 'suyumbaeva', 'age': 17, 'gender': 'j', 'birthday' : '08.08.2005'}

passport['name'] # 'aigerim

# print(passport.get('age')) # 17
# print(passport.get('ID'))  # None

# dict.get(key, None) - отдает значение указанного ключа, если нет - отдает второе указанное значение (по умолчанию None)

# print(passport.get('ID', 'no key')) # no key


# passport.setdefault(key, default) - отдает значение указанного ключа, 
# если его нет - создает его со значением default( по умолчанию - None)

# passport.setdefault('age') # 17
# # print(passport.setdefault('ID')) # None

# print(passport.setdefault('ID', 73874892)) # 'ID': 73874892
# print(passport)


# passport.update({key: value}) - принимает в себя другой словарь и обновляет исходный за счет него 
# passport.update({'ID': 777})
# print(passport)

dict8 = {'name': 'vasya', 'age': 99, 'name': 'kolya' , 'ID': 999}
# print(dict8) # {'name': 'kolya', 'age': 99}
# passport.update(dict8)
# print(passport)


# a = {'a': 10, 'b': 20}
# # a['c'] = 30  добавляет новй ключ 
# a['b'] = 40 # меняет значение 20 на 40 
# print(a) # 'a': 10, 'b': 20, 'c': 30

dict10 = {'name': 'vasya', 'last_name': 'pupkin', 'age': 21}

# dict10.pop('name') # удаляет указанный ключ и возвращает удаленный ключ
# print(dict10) # {'last_name': 'pupkin', 'age': 21}

# dict10.pop('ID')
# print(dict10) # KeyError 'ID'

# deleted_key = dict10.pop('ID' , 'no key')
# print(deleted_key) # no key
# print(dict10)      # {'name': 'vasya', 'last_name': 'pupkin', 'age': 21}

# deleted_el = dict10.popitem() # удаляет последнюю пару словаря и возвращает ее в виде кортежа(tuple)
# print(deleted_el)  # ('age': 21)
# print(dict10)    # {'name': 'vasya', 'last_name': 'pupkin}


# dict10.clear()
# print(dict10) # {}

# del dict10['age']
# print(dict10) # {'name': 'vasya', 'last_name': 'pupkin}

iter_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# for iter in iter_dict:
#     print(iter) # keys

# for i in iter_dict:
#     print(iter_dict[i])

''' keys(), values(), items() '''

k = iter_dict.keys()
# print(k)  # dict_keys(['a', 'b', 'c', 'd'])
# for key in k:
#     print(key)

v = iter_dict.values()
# print(v) # dict_values([10, 20, 30, 40])
# for values in v:
#     print(values)

it = iter_dict.items()
# print(l) # dict_items([('a',10), ('b' 20), ('c' 30), ('d' 40)])
# for key, value in it:
#     print(f'keys: {key}  values: {value}')

contacts = {
    'names': {
        'vasya': 996700200300 ,
        'kolya': 996702002003 ,
        'igor':  996700666666
    }
}

# # print(contacts['names']['igor'])
# names = contacts['names']
# print(names['vasya'])

# copy() -копирует словарь
# contacts_copy = contacts.copy()
# print(contacts_copy)

