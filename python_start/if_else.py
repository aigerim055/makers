'''условные выражения'''

# >
# < 
# ==  
    # --> bool()
# !=
# >=
# <=

# print(20>10)
# print(15<5)

# print(bool(0)) #False
# print(bool(1)) #True
# print(bool(2)) #True - все цифры кроме нуля(0)будут TRUE

bool('') #False
bool([]) #False
bool({}) #False
bool(set()) #False
bool(None) #False

''' if '''
# num = 15
# if num > 16:
#     print('hello')

''' else '''
# num = 15
# if num > 16:
#     print('hello')
# else:
#     print('goodbye')


# temp = 40
# if temp < 20:
#     print('cold')
# else:
#     if temp < 30:
#         print('warm')
#     else:
#         if temp > 35:
#             print('hot')

''' elif '''
# temperature = 40
# if temperature < 20:
#     print('cold')
# elif temperature < 30:
#     print('warm')
# elif temperature < 35:
#     print('hot')
# else:
#     print('very hot')

# num = 15 
# if num < 20:
#     print('ok')
# if num > 10:
#     print('same')
# if num < 23:   
#     print('good')
#

# mark = int(input('vvedite osenku ot 1 do 10: '))
# if mark == 10:
#     result = 5
# elif mark < 3:
#     result = 2
# elif mark < 5:
#     result = 3
# else:
#     result = 4
# print(result)


# if условие:
#     действие
# elif условие:
#     drugoe_действие
# else:
#     действие в случае если ни одно из выше указанных условий не сработало

# in - проверка на вхождения
# string = 'Hello!Как твои дела?'
# if 'hello' in string.lower():
#     print('hi')
# else:
#     print(';-(')

# string = 'Hello! How are you?'
# if 'hello' not in string.lower():
#     print(';-(')
# else:
#     print('hi :)')

'''and, or, not'''

False and False #False
True and True   #True
False and True  #False
True and False  #False

# age = 19
# if age > 15 and age < 18:
#     print('ok')
# else:
#     print('not ok')

False or True  #True
True or False  #True
False or False #False
True or True   #True


# age = 19
# if age > 15 or age < 18:
#     print('ok')
# else:
#     print('not ok')

not False #True
not True  #False

# print(int(False)) #0
# print(int(True))  #1
True + True #2

a = 10
print(['ok' , 'not ok'][a > 10]) #ok
print(['ok' , 'not ok'][a > 5])  #not ok


