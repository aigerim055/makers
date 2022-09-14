'''  полиморфизм '''

#  полиморфизм - принцип ООП, который заключается в использовании одной сущности(метод, оператор) для различных типов объектов

# # +
# num1 = 10
# num2 = 30
# print(num1 + num2) # сложение - 40

# str1 = 'helllo'
# str2 = 'world'
# print(str1 + str2) # конкатенация - helloworld


# class A:
#     def method1(self):
#         return 10 + 10

# class B:
#     def method1(self):
#         return 'method1'

# obj_a = A()
# obj_b = B()
# for obj in (obj_a, obj_b):
#     print(obj.method1())

# class Cat:
#     def meow(self):
#         print('meow')

# class Dog:
#     def bark(self):
#         print('bark')

# cat = Cat()
# dog = Dog()

# for animal in (cat, dog):
#     if type(animal) is Cat:
#         animal.meow()
#     else:
#         animal.bark()

# class Cat:
#     def sound(self):
#         print('meow')

#     def __str__(self):
#         return 'я кошка'

# class Dog:
#     def sound(self):
#         print('bark')

#     def __str__(self):
#         return 'я собака'

# cat1 = Cat()
# dog1 = Dog()

# for animal in (cat1 ,dog1):
#     animal.sound()


# print()
# len()


