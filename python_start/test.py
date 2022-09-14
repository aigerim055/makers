
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


#TAsk7
# num = 7
# def check(num):
#     if num %2 == 0:
#         print("It is even number")
#     else:
#         print("It is odd number")
#     return num
# check(num)



# def ispalindrom(string):
#     if string == string[::-1]:
#         print(True)
#     else:
#         print(False)
#     return string
# ispalindrom(101)

# x = 'Я глобальная переменная!'
# def my_func():
#     global x
#     x = 'Я могу изменяться'
#     return x
# print(x)
# print(my_func())

# num = 3
# def mul():
#     global num 
#     num = num ** 2

# mul()
# mul()
# mul()
# print(num)

'''
Напишите небольшую программу для подсчета доходов и расходов.

У вас есть глобальная переменная balance = 0 общий счет.

Программа должна состоять из трех функций: 
get_salary(amount) - функция для увеличения баланса, которая принимает в аргументы amount - 
заработная плата и увеличивает переменную balance на число переданное в amount.

pay_bills(amount, log_name) - уменьшает баланс на количество amount , log_name - принимает строку 
- на что были потрачены деньги и распечатывает результат, например если мы вызвали pay_bills(300, 'интернет')

И функция (get_balance()), которая будет распечатывать вам строку:

У вас на счету `n` сом
где n - это текущее значение глобальной переменной balance.

Вызовите функции в данном порядке:

get_salary(1000)
get_balance()
pay_bills(400, 'кабельное тв')
get_balance()

'''


# balance = 0

# def get_salary(amount):
#     global balance
#     balance += amount


# def pay_bills(amount, log_name):
#     global balance
#     balance -= amount
#     log_name = print(f'Вы заплатили {amount} сом за {log_name}')

# def get_balance():
#     global balance
#     print(f'У вас на счету {balance} сом')

# get_salary(1000)
# print(get_balance())
# print(pay_bills(400, 'кабельное тв'))
# print(get_balance())



#TASK5
# result = 0
# def pow_first(num1: int, num2: int) -> int:
#     global result
#     result = num1 ** num2
    

# def pow_second(z:int) -> int:
#     global result
#     result %= z

# pow_first(2, 3)
# pow_second(3)
# print(result)

# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}


# # def age_control():
# for k,v in a.items():
#     if v >= 18:
#         print(f'{k}, Вы можете войти в клуб') 
#     else:
#         print(f'{k}, извините, Вы не проходите по age-control')
# # age_control()

# a = ['vasya', 'kolya', 'sasha']
# b = []
# for i in a:
#     b.append(i.title())
# print(b)

# a = []

# for i in range(11):
#     a.append(i)
# print(a)



# def get_count(string):
#     counter = 0
#     for i in string:
#         if i in 'aeiou':
#             counter += 1
#     return counter
# print(get_count('hello'))



# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# def open_or_senior(data):
#     output = []
#     for age, handicap in data:
#         if age >= 55 and handicap > 7:
#             output.append('Senior')
#         else:
#             output.append('Open')
#     return output

# # print(open_or_senior(input))

# dict_ = {'key1': 'value1', 'key2': 'value2'} 
# try:
#     print(dict_['key33'])
# except KeyError:
#     print('Нет такого ключа!')


# try:
#     age = int(input())
#     if age < 18:
#         raise ValueError ('Доступ запрещен!')
# except TypeError:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')

# def decarator_func(func):
#     def wrapper():
#         print('hello')
#         func()
#         print('goodbue')
#     return wrapper

# def some_func():
#     print('вфзщв функции some func')


# some_func = decarator_func(some_func)
# some_func()

# result = 0
# def pow_first(x,y):
#     global result
#     result = x ** y
#     return result

# def pow_second(z):
#     global result
#     result %= z
#     return result

# pow_first(2, 3)
# pow_second(3)
# print(result)


# dict_ = {'key1': 1, 'key2': 2}
# def dictionary():
#     for k in dict_.keys():
#         print(k)

# # dictionary()

# num = 7
# def check(num):
#     if num %2 == 0: 
#         return 'It is odd number'
#     else:
#         return 'It is even number'
# print(check(num))

# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {k: list(range(1,v + 1)) for k,v in a.items() }
# print(dict_)
# for k,v in a.items():
#     v += 1
#     a[k] = list(range(1,v))

# print(a)




# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [str for str in string_.split() if str.isdigit() ]
# print(list_)
# for str in string_.split():
#     if str.isdigit():
#         list_.append(str)
# print(list_)


# try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1 % num2)
# except (ZeroDivisionError, ValueError):
#     print('Произошла ошибка!')

# cash = int(input())
# if cash < 0:
#     raise ValueError ('Сумма не может быть отрицательной! ')
# # except ValueError:
# #     print('Сумма не может быть отрицательной! ')
# else:
#     print(cash)

# list_ = [-1, 2, 3, 0, 5, -3,7] 
# for i in list_:
#   print(i)
#   if i < 0: 
#     list_.append('False')
#   else:
#     list_.append('True')

# print(list_)

# list_ = [1, 5, -9, 6, -4] 
# result = all(num > 3 for num in list_ )
# print(result)

# list_ = [5, 8, 4, 6, 7]
# result = any(num < 0 for num in list_)
# print(result)

# list_ = [1, 2, 3, 4] 
# result = list(map(lambda num1: num1 ** 2, list_))
# print(result)


# list_ = [1, 2, 3, 4] 
# result = list(filter(lambda num: num % 2 == 0, list_))
# print(result)

# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',]
# result = list(filter(lambda str: len(str) > 7, list_))
# print(result)


# list_ = [5, 6, 7, 8] 
# result = reduce(lambda num1, num2: num1 * num2, list_)
# print(result)

# TASK8
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 
# list2 = list(filter(lambda num: num % 2 == 0, list_))
# list3 = list(filter(lambda num: num % 2 != 0, list_))
# result = f'even: {len(list2)}, odd: {len(list3)}'
# print(result)

# list_ = [-1, 2, 3, 5, -3, 7] 
# result = list(map(lambda num: False if num < 0 else True, list_))
# print(result)

# from functools import reduce
# list_ = ['Paul', 'George', 'Ringo', 'John'] 
# def func(name1, name2):
#     if len(name1) > len(name2):
#         return name1
#     return name2
# result = reduce(func , list_  )
# print(result)

# dict_ = {'a': 5, 'a': {'a': 1}}
# print(dict_)

# a = set([1], [2])
# print(a)

# y = 2

# x = list(lambda x: x + 2, y)
# print(x)

# try: 
#     a = 1
#     b = 2
#     print(c)
#     exit
# except NameError:
#     print('nnno')
# else:
#     print('yes')
# finally:
#     print('hello')

# print(locals())
# print(globals())


# list_ = [1,2 ,3, 4]
# list1 = map(lambda x: x % 2 == 0, list_)
# print(list(list1))

# list2 = filter(lambda x: x % 2 == 0, list_)
# print(list(list2))

# list1 = [1, 2, 4]
# list2 = [1, 3, 4]
# new_list = list1 + list2

# print(sorted(new_list))



# file1 = open('task5.txt')
# numbers = []

# for line in file1:
#     numbers.append(int(line))

# file2 = open('task6.txt', 'w')

# print(file2.write(f"{min(numbers)}-{max(numbers)}"))

# file1.close()
# file2.close()

# from functools import reduce
# list_ = [1, 2, 3, 4]
# result = reduce(lambda x: x ** 2, list_)
# print(result)

'''
Создайте класс MyDict который будет наследоваться от встроенного класса dict. Переопределите метод get() таким образом, 
чтобы при попытке получения несуществующего ключа, по умолчанию он возвращал, вместо None, строку:

Are you kidding?
Создайте экземпляр класса в переменной 'obj_dict' и попробуйте получить несуществующий ключ методом get().

Например:

obj_dict = MyDict({'some_title': 2}) 
print(obj_dict.get('some')) 
Ключа 'some' в нашем словаре нет, есть только 'some_title', в терминале получим:

Are you kidding? 
Метод get имеет такой синтаксис: словарь.get(ключ, значение), в значение передается то что вы хотите возвратить если такого ключа не существует. 

По умолчанию, если второе значение не передано, метод возвращает None. Для переопределения метода унаследуйте метод от родителя и передайте в метод 
свое значение.
'''





# class MyDict(dict):
#     def get(self, key, default = 'are you kidding me?'):
#         return dict.get(self, key, default)

# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some')) 


'''
Создайте класс Person который будет описывать человека, а точнее его имя - name и возраст - age. Добавьте к классу метод display(), 
который будет выводить данные об этом человеке.

Создайте второй класс Student, который будет наследоваться от класса Person.

Объекты от класса Student должны иметь все атрибуты, которые были определены в родительском классе и еще один дополнительный атрибут - 
faculty, который будет описывать факультет, где учится студент.

Создайте метод display_student(), который будет выводить данные об этом студенте.

Создайте от класса Student объект в перемнной obj_student, и выведите данные о нём, как о человеке, затем как о студенте.

'''

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         return f'name: {self.name}, age: {self.age}'

# class Student(Person):
#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty

#     def display_student(self):
#         return f'{super().display()}, faculty: {self.faculty}'

# obj_student = Student('vasya', 33 , 'scince')
# print(obj_student.display())
# print(obj_student.display_student())


'''
Создайте класс SmartPhones, экземпляры класса должны иметь такие свойства:

name - название
color - цвет
memory - память
battery - процент заряда батареи
Значение battery по умолчанию должно быть 0.

Переопредилите метод str так чтобы при распечатке он выдавал строку с названием и памятью смартфона.

У данного класса также должен быть метод charge, который увеличивает значение батареи на указанную величину.

Создайте два дочерних класса от Smartphones:

Iphone - с дополнительным аттрибутом экземпляра - ios и методом send_imessage(принимает в аргументы строку 
и возвращает эту строку и от какого телефона сообщение было выслано в таком формате - sending 'ваша строка' from 'название объекта-телефона')

Samsung - с дополнительным аттрибутом android и методом show_time(который показывает текущее время)

Создайте объекты phone, iphone7, samsung21 от классов SmartPhones, Iphone, Samsung и примените все методы.

Для правильной работы тестов, проделайте все следующие операции:
'''

# from datetime import datetime



# class SmartPhones:
    
#     def __init__(self, name, color, memory, battery = 0):
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = battery
        

#     # def charge(self, int):
#     #     self.int = int
#     #     f = self.battery + int
#     #     return f

#     def charge(self,plus_battery):
#         self.battery += plus_battery
#         return self.battery

#     def __str__(self):
#         return f'{self.name} {self.memory}'



# class Iphone(SmartPhones):
#     def __init__(self, name, color, memory, ios, battery = 0):
#         self.ios = ios
#         super().__init__(name, color, memory, battery)


#     def send_imessage(self, string):
#         self.string = string
#         return f'sending {string} from {self.__str__()}'


# class Samsung(SmartPhones):
#     def __init__(self, name, color, memory, android, battery = 0):
#         self.ios = android
#         super().__init__(name, color, memory, battery)

#     def show_time(self):
#         t = datetime.now().time()
#         return t




# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone) 

# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery) 

# iphone7 = Iphone('Iphone 7', 'gold', '128gb','12.1.3') 
# print(iphone7)
# print(iphone7.send_imessage('hello')) 

# samsung21 = Samsung('Samsung A21', 'black', '256gb' , 'Oreo') 
# print(samsung21.show_time())


'''
Создайте класс ContactList, который должен наследоваться от встроенного класса list.

В вашем классе должен быть реализован метод search_by_name, который должен принимать имя и возвращать список всех совпадений.

Создайте экземпляр класса в переменной all_contacts и передайте список ваших контактов.
'''

# class ContactList(list):

#     def __init__(self, f = list):
#         self.f = f

#     result = []

#     def search_by_name(self, string):
#         result = [elem for elem in self.f if string in elem]
#         return result

# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya'))

# class Circle:
#     color = 'blue'
#     pi = 3.14

#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
        
#         res = self.pi * (self.radius ** 2)
#         return res

# circle = Circle(2) 
# circle.get_area()

'''
Создайте класс BankAccount, у объектов данного класса есть аттрибут balance со значением по умолчанию 0: balance = 0.
Определите метод withdraw с параметром amount, который будет отнимать сумму от баланса и распечатывать текущий баланс.
Добавьте еще один метод deposit, который также имеет параметр amount и соответсвенно добавляет сумму к балансу и распечатывает баланс.
'''

# class BankAccount:

#     def __init__(self, balance = 0 ):
#         self.balance = balance

#     def withdraw(self, amount):
#         self.amount = amount
#         self.balance -= amount
#         print(f'Ваш баланс: {self.balance} сом')


#     def deposit(self, amount):
#         self.amount = amount
#         self.balance += amount
#         print(f'Ваш баланс: {self.balance} сом')

# account = BankAccount()
# account.deposit(1000) 
# account.withdraw(500) 


'''
Задание 4
Создайте класс Taxi, объекты которого имеют такие атрибуты как название компании - name, стоимость посадки - cost, 
стоимость за каждый пройденный километр - cost_km.
Добавьте к классу метод get_total_cost, принимающий параметр km - сколько километров составила поездка и возвращающий стоимость поездки.
Создайте три экземпляра класса Taxi для трех разных компаний Namba, Yandex и Jorgo и расчитайте стоимость поездки на каждой из них.
'''

# class Taxi:
#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km

#     def get_total_cost(self, km):
#         self.km = km 
#         price = self.cost + self.cost_km * km
#         res = f'Такси {self.name}, стоимость поездки: {price} сом '
#         return res

# taxi1 = Taxi('Namba', 10, 33)
# taxi2 = Taxi('Yandex', 21, 4)
# taxi3 = Taxi('Jorgo', 12, 11)
# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))  

'''
контактов должны быть такие аттрибуты:

name - имена
last_name - фамилии
phone - телефонные номера
Добавьте метод get_info, который выводит информацию о контакте в следующем виде:

contact.get_info()
Вывод в терминал:

Контакт: John Snow, телефон: +996707707707
Затем, создайте объект от класса Phone в переменной contact и примените метод get_info.
'''

# class Phone:

#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone

#     def get_ingo(self):
#         i = f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}'
#         print(i)

# contact = Phone('John', 'Snow', '+996707707707')
# contact.get_ingo()


'''
Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - percent = 8, 
обозначающий процент налога на ежемесячную зарплату - 8%.

Объекты класса должны иметь, в качестве атрибутов сумму зарплаты salary и стаж работы в месяцах - experience.

Также у класса должен быть метод count_percent, расчитывающий сумму налога заплаченного за весь стаж работы.

Создайте экземпляр класса obj и посчитайте сумму вашего налога.

К примеру, если у вашего объекта salary имеет значение 10000, а experience равен 10, то:

print(obj.count_percent()) 
Выдаст вам такой результат в терминале:

8000.0 
Каждый месяц с зарплаты в 10000 сомов снимается 8% на налоги, т.е 800 сом, за 10 месяцев трудового стажа эта сумма будет 8000.0 сом
'''

# class Salary:
#     percent = 8

#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.experience = experience

#     def count_precent(self):
#         tax_per_month = self.salary / 100 * self.percent
#         result = self.experience * tax_per_month
#         return result

# obj = Salary(8000, 10)
# print(obj.count_precent()) 


'''
Задание 8
Создайте класс Password, экземеплярами класса являются пароли в виде строк. У класса должен быть метод validate для валидации пароля:

В начале, проверьте, что пароль состоит из минимум 8 символов, но меньше 15, если условие не соблюдено, должны выйти ошибка с текстом:
Password should be longer than 8, and less than 15
Вторая проверка должна проверять что пароль содержит цифры, и в случае отсутствия цифр, выводить ошибку с текстом:
Password should contain numbers too
Третья проверка, проверяет содержит ли пароль буквы и в случае не совпадения, выводит ошибку с текстом:
Password should contain letters as well
В конце проверьте, содержит ли пароль хотя бы один из символов: '@', '#', '&', '$', '%', '!', '~', '*', если условие не выполнено выводите ошибку с текстом:
Your password should have some symbols
если одно из условий не выполнено, выводите соответствующее исключение, если же все условия выполнены метод validate должен возвращать строку:

Ваш пароль сохранен.
Также переопределите метод __str__, чтобы при попытке распечатать сам пароль, вам выдавалась строка из звездочек количество которых равно длине пароля.

К примеру, если пароль joe@123456, при попытке распечатать пароль, в терминал должно выводиться: **********

пишите код для проверки пароля в указанном порядке
'''

# from curses.ascii import isalpha, isdigit


# class Password:

#     def __init__(self, password: str):  
#         self.password = password

#     def validate(self):
#         p = self.password

#         if len(p) > 8 and len(p) < 15:
#             return 'Password should be longer than 8, and less than 15'
#         if p.isdigit() == False:
#             return 'Password should contain numbers too'
#         if p.isalpha() == False:
#             return 'Password should contain letters as well'
#         if p ==  '@, #, &, $, %, !, ~, *':
#             return 'Your password should have some symbols'
#         else:
#             return 'Ваш пароль сохранен!'

#     def __str__(self):
#         pass_length = len(self.password)
#         return pass_length * '*'

# password = Password('we@#3fdfe')

# print(password.validate())

'''
Создайте класс Math, у экземпляра которого должно быть свойство value. У классa Math должно быть 3 метода:

get_factorial - возвращает факториал числа(перемножить все составные числа до самого числа)

get_sum - возвращает сумму цифр числа

get_mul_table - возвращает таблицу умножения для числа до 10 в формате:

5x1=5
5x2=10
5x3=15
5x4=20
5x5=25
5x6=30
5x7=35
5x8=40
5x9=45
5x10=50
Создайте экземпляр класса и примените к нему все методы.

Например, если экземпляром класса Math является число 11,

вызов get_factorial возвратит такой результат:

39916800 
т.к 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 x 9 x 10 x 11 = 39916800

метод get_sum, возвратит:

2 
т.к число 11 состоит из двух цифр 1 и 1, сумма 1 + 1 = 2

метод get_mul_table возвратит:

11 x 1 = 11 
11 x 2 = 22 
11 x 3 = 33 
11 x 4 = 44 
11 x 5 = 55 
11 x 6 = 66 
11 x 7 = 77 
11 x 8 = 88 
11 x 9 = 99 
11 x 10 = 110 
результат методов возвращайте ключевым словом return, print() использовать не надо.
'''
# import math

# class Math:
#     def __init__(self, value):
#         self.value = value
    
#     def get_factorial(self):
#         fact = math.factorial(self.value)
#         return fact

#     def get_sum(self):
#         num_list = list(map(int, str(self.value)))
#         result = sum(num_list)
#         return result

#     def get_mul_table(self):
#         result = ''
#         num_list = list(range(1, 11))
#         for num in num_list:
#             line = self.value * num
#             result += f'{self.value}x{num}={line}\n'
#         return result

# num = Math(11)

# print(num.get_factorial())
# print(num.get_sum())
# print(num.get_mul_table())




'''
Создайте класс A и объявите в нём 3 метода:

публичный(public) (возвращает строку 'Public method'),
защищённый(protected) (возвращает строку 'Protected method')
приватный(private) (возвращает строку 'Private method')
Затем создайте экземпляр в переменной obj1 данного класса и вызовите (с выводом в терминал)
по очереди каждый из методов. Не забудьте, что нужно вызвать приватный метод так, чтобы ошибка не выводилась
'''

class A:
    def public(self):
        return 'Public method'

    def _protected(self):
        return 'Protected method'

    def __private(saelf):
        return 'Private method'

obj = A()
print(obj.public())
print(obj._protected())
print(obj._A__private())