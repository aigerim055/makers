''' инкапсуляция
1. ограничение доступа к опр данным
2. объединение атрибутов и методов, котрые работают с данными в один класс
'''

# инкапсуляция в питоне реализована на уровне соглашения 

''' 
модификаторы доступа:
1. public
публичные атрибутяы и мтоды доступны в классе, в дочерних класса и вне класса

2. protected
защищенные атрибуты и метооды доступны в классе, в дочерних классах, но не доступны вне класса

3. private
приватные атрибуты и методы доступны только внтури того класса где они определены
'''

class EncapsulatedClass:
    public = 'public'
    _protected = 'protected'
    __private = 'private'

    def pub_method(self):
        pass

    def _prot_method(self):
        pass

    def __private_method(self):
        pass


# enc = EncapsulatedClass()
# print(enc.public ) # public
# print(enc._protected) # protected
# # print(dir(enc))
# # print(enc.__private) # attributeError
# print(enc._EncapsulatedClass__private) # private


class InheritClass(EncapsulatedClass):
    pass

inh = InheritClass()
# # print(dir(inh))
# print(inh.public)
# print(inh._protected)
# print(inh._EncapsulatedClass__private)

''' setter & getter - интерфейсные методы '''

class Light:
    __turned_on = False

    def __init__(self, brightness):
        self.__brightness = brightness

    # setter
    def set_status(self):
        self.__turned_on = True

    # getter
    def get_status(self):
        return self.__turned_on

    @property # getter
    def brightness(self):
        return self.__brightness

    @brightness.setter # setter
    def btightness(self, value):
        self.__brightness = value

    # brightness = property(get_brightness, set_btightness)



lamp = Light(50)
# lamp._Light__turned_on = True # неправильный способ
# lamp.set_status()
# print(lamp.get_status())
# print(lamp.brightness) # сработал get_....
# lamp.brightness = 70   # сработал set_...
# print(lamp.brightness)





class Car:
    __MAX_SPEED = 300
    __MIN_SPEED = 0

    def __init__(self, color, model, max_speed, min_speed):
        self.color = color
        self.model = model
        self.max_speed = max_speed
        self.min_speed = min_speed

        if self.validate():
            raise ValueError('не правильно указана скорость')
       
    def validate(self):
        return self.max_speed > self.__MAX_SPEED or self.min_speed < self.__MIN_SPEED



car1 = Car('black', 'Toyota', 350, 0)
