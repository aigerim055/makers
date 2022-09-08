# DRY - dont repeat yourself

''' наследованиие - процесс, когда один класс происходиит от другого класса  '''

# class Parent: # родительский класс(базовый), base class
#     pass

# class Child(Parent): # дочерний класс(производный), child, inherited class
#     pass


# class Parent:
#     hands = 2
#     yeys = 2

#     def _draw(self):
#         print('родитель хорошо рисует')

# class Child(Parent):
#     pass

# child = Child()
# child._draw()

''' при наследовании дочерние классы перенимают все атрибуты и методы род класса'''

# class Animal:
#     def sound(self):
#         print('животное издает звук')

#     def run(self):
#         print('животное бежит')


# class Cat(Animal):
#     def sound(self):
#         print('Мяу')

#         ''' переопределение метода - полное изменение поведение метода '''


# class Dog(Animal):
#     def run(self):
#         super().run() # дпоплнени метода
#         print('собака бежит')

#         ''' super() - функция для обращения к род классу'''


# a = Cat()
# a.sound()

# b = Dog()
# b.run()

# class A:
#     attr1 = 10

#     def mul(self):
#         return self.attr1 * 2

# class B(A):
#     attr2 = 10

#     def mul(self):
#         par = super().mul()
#         return par + self.attr2

# res1 = A()
# res = B()

# print(res1.mul()) # 20
# print(res.mul()) # 30


''' наследоваться можно от встроенных классов '''

# class MyStr(str):
#     def first(self):
#         return self[0]

#     def last(self):
#         return self[-1]

#     def upper(self):
#         print('преведено в вверхний регистр')
#         return super().upper()

#     # print(locals())



# str1 = MyStr('hello wrold')
# # print(str1.first()) # h
# # print(str1.last())  # d
# # print(str1.upper()) # HELLO WORLD

# # print(issubclass(MyStr, (str, int , list))) # True

# print(str1.upper())


# class Person:
#     def __init__(self, name, lastname, age):
#         self.name = name
#         self.lastname = lastname
#         self.age = age


# class Student(Person):
#     def __init__(self, name, lastname, age, course, faculty):
#         super().__init__(name, lastname, age)
#         self.course = course
#         self.faculty = faculty


# p = Person('vasya', 'pupkin', 24)
# print(dir(p))

# object -> Person -> Student


''' можественное наследование '''

# class A:
#     def m1(self):
#         print('method A')

# class B:
#     def m2(self):
#         print('method 2')

# class C(A, B):
#     pass


# res = C()
# res.m1()
# res.m3()

