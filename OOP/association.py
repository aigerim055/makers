''' ассоциация (агрегация, композиция)'''



''' агрегация '''
class Battery:
    def __init__(self):
        self.power = 100

class Electronic:
    def __init__(self, model,color):
        self.model = model
        self.color = color
        self.battery = Battery()

class Phone(Electronic):
    pass

class Laptop(Electronic):
    pass

phone = Phone('samsung', 'black')
phone.battery.power # 100
bat = Battery()


''' композиция '''
class Human:
    class Heart:
        def __init__(self):
            self.heart = '4-хкамерное'

    class Kidneys:
        def __init__(self, q):
                self.q = q 
 
    class Eyes:
        def __init__(self, eyes_color):
            self.eyes_color = eyes_color
    
    def __init__(self, q, eyes_color):
        self.heart = self.Heart()
        self.kidneys = self.Kidneys(q)
        self.eyes_color = self.Eyes(eyes_color)

h = Human(2, 'black')
e = Human.Heart()