''' миксины  '''

# mixin - это классы, которые исп для дополнения функционала других классов путем наследования. от миксинов нельзя создавать объекты


# class MicrowaveMixin:
#     def heat(self):
#         print('греет еду')

# class Fridge:
#     def cold(self):
#         print('охлаждаю еду')

# class TV:
#     def watch_tv(self):
#         print('передаю шоу')

# class Cooker:
#     def cook(self):
#         print('готовлю еду')



# class Kitchen(MicrowaveMixin, TV, Cooker, Fridge):
#     p = 10

# obj = Kitchen()
# obj.watch_tv()

class BaseClass:
    def eat(self):
        pass

class BaseMixin:
    def eat(self):
        print('я много ем')

class ChuldrenClass(BaseMixin, BaseClass):
    pass

obj = ChuldrenClass()
obj.eat()

# при наследовании от миксинов и других классов - миксины нужно указывать в первую очередь (MRO)