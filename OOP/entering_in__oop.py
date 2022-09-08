''' ООП - объектно ориентированное програмирование '''

# классы - участок кода. который описывает какой-то объект/тип данных. 

# class MyClass:
#     a = 10 # атрибут класса

# атрибут класса - это атрибут/переменная класса, которая относиться ко всем мозданным объектам/экземплярам класса. 
# у каждого объекта есть своя копия атрибутов

# class Human:
#     skin = True
#     hands = 2
#     head = 1


# h = Human() # объект/экземпляр класса
# # print(type(h))
# # print(h.hands)
# h.hands = 3
# print(h.hands)
# h2 = Human()
# print(h2.hands)


# class Human:
#     hands = 2
#     head = 1
#     legs = 2

#     def __init__(self, age, height, weight):
#         self.age = age
#         self.height = height
#         self.weight = weight
#         # атрибуты экземпляра класса - атрибуты присущие конкр объекту/экземпляру 


# human1 = Human(20, 185, 80)
# human2 = Human(height=175, age=23, weight=65)
# print(human1.age)
# print(human2.age)


# метод - это функция, которая определена внутри класса и описывает какое-то действие


# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         # self - ссылка на объект класса
#         print(f'{self.name} лает')

# dog1 = Dog('tuzik')
# dog1.bark()
# Dog.bark(dog1)



# class Student:
#     course = 4

#     def __init__(self, name, lastname, age):
#         self.name = name
#         self.lastname = lastname
#         self.age = age

#     def get_info(self):
#         return f'{self.name} {self.lastname} , {self.age} года'

#     def sleep(self):
#         print(f'студент: {self.name}')
#         print('спать во время занятий')

#     def write(self):
#         print('пишу лекции')




# student1 = Student('Sregei', 'Pupkin', 23)
# student2 = Student('Vasya', 'Pupkin', 22)
# student1.sleep()
# print(student2.get_info())
# student1.write()



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bd(self):
#         self.age += 1
#         return f'happy birthday {self.name}!! \nВам теперь {self.age} лет'



# person1 = Person('Vasya', 24)
# print(person1.age)
# print(person1.bd())
# print(person1.age)

# person1.legs = 3
# print(person1.legs)


# class Car:
#     car_counter = 0

#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#         Car.car_counter += 1


#     def __str__(self) -> str:
#         return f'color: {self.color} \nmodel: {self.model}'


# car1 = Car('green', 'Toyota')
# # print(car1.car_counter)
# car2 = Car('blue', 'Mersedes')
# # print(car2.car_counter)
# print(car1)

# type(obj) - позволяет узнать тип объекта

# isinstance(obj, class) - возвращает True/False, если переданный объект принадлежит указанному классу

# print(isinstance(12, int))

# int 
# list
# dict
# tuple
# set
# bool
# frozenset

'''
основные принципы ООП:
1.наследование
2.инкапсуляция
3.полиморфизм

не основные принципы ООП: 
4.агрегация
5.абстракция
6.композиция
'''

