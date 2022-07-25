# int() 
# float()

'''matematicheskie operatory'''

# num1 = 15
# num2 = 3

# num1 + num2 - slojenie
# num1 - num2 - vychitanie
# num1 * num2 - umnojenie
# num1 / num2 - delenie  -> float()
# num1 ** num2 - stepen'
# num1 // num2 - delenie bez ostatka -> int()
# num1 % num2 - vydelenie ostatka ot deleniya -> int()


from decimal import Decimal
desimal1 = Decimal('0.1')
desimal2 = Decimal('0.1')
desimal3 = Decimal('0.1')
# print(desimal1 + desimal2 + desimal3)


'''funksii'''
abs(-5)  #5
abs(-2.4) # 2.5
# abs(x) - возвращает модуль переданного числа

pow(2 , 3 ) # 2 ** 3
pow(2 , 3 , 4) # 2** 3 % 4
# pow(x , y [z]) - vozvodit v spepen'

divmod(1 , 2) # 1 // 2, 1 % 2 - (0 , 1) 
# divmod(x , y) 

round(2.3) # 2
round(2.6) # 3
round(2.5) # 2 - okruglaet v men'shuiu storonu
round(2.3456 , 2) # 2.35
# round(x[y]) - okruglenie peredannogo chisla do zelogo


import math # biblioteka dlya matematicheskix raschetov

# math.sqrt(25) # 5 sqrt - kvadratnyi koren'
# math.factorial(5) # 120
# 1 *2 * 3 * 4 * 5 - math.factorialchisla 5
# math.pi =  chislo pi


# num1 = float(input('vvedite pervoe chislo: '))
# num2 = float(input('vvedite vtoroe chislo: '))
# print('result: ',num1 + num2)


# x = 1
# x + 1 
# print(x) # 

# x = 2
# x = x + 1
# print(x) #  3

# x = 3
# x += 1 # x = x + 1
# print(x) # 4

