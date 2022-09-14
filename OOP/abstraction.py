''' абстракция '''
# абстракция - сущность без конкретной реализации

# class Animal:
#     def __init__(self):
#         self.eat()
#         self.move()
#         self.sound()


#     def eat(self):
#         raise NotImplementedError(self.__class__.__name__)

#     def sound(self):
#         raise NotImplementedError(self.__class__.__name__)
    
#     def move(self):
#         raise NotImplementedError(self.__class__.__name__)

# class Cow(Animal):
#     pass


# cow = Cow()
# cow.eat()



from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def get_x(self):
        return 'x'

    @abstractmethod
    def abc_method(self):
        pass

class ConcreteClass(AbstractClass):
    def method1(self):
        print(12121)

    def abc_method(self):
        return 'hello world'

a = ConcreteClass()
# print(a.get_x())