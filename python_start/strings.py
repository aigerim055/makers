'''строки'''

# str()
# строки - это неизменяемый , упорядочунный , indeksirovannyi  тип данных


# string = " hello "


string2 = ' hello '

doc_string = ''' обычно исп для написания документации
к коду '''

string3 = "helllo, I'm student"

string4 = 'hello, I\'m student'

# str1 = 'hello'
# str2 = 'world'
# print(str1 + str2)
#конкатенация - склеивание строк

# str3 = 'Quak'
# num1 = 3
# print(str3 * num1)

'''функции и методы строк'''
my_str = 'hello world'

# print(len(my_str)) #vyvodit dlinu stroki
# print(my_str.split(Separator)) #delit po ukazannomu delitelu(po umolchaniyu - probel)
my_str.replace('l' , 'b') #hebo worbd -zamena podstroki v stroke
my_str.upper() # HELLO WORD - perevod v vverxniy registr
my_str.lower()  # hello world - perevod v nijniy  registr
my_str.title() # Hello World - perevod pervogo simvola kajdogo slova v verxniy registr
my_str.capitalize() # Hello world - perevod pervogo simvola stroki v vverxniy registr
'ß'.casefold() #  'ß ' - ss
my_str.count('l')  # 3 - schitaet colichestvo jojdeniy peredannoi podstroki

'''индексы и срезы'''
str7 = 'hello world'
# индекс - это порядковы номер символа в строке(nachinaya s 0)
# 'makers'
#  012345
# -054321
# print(str7[4])
# print(str7[10])
# print(str7[len(str7)-1])
# print(str7[-1])

# print(str7[0:5]) # hello
# str[start:stop]

# print(str7[4:])  # ot starta do konca stroki
# print(str7[:7])    ot nachala do ukazonnogo indeksa
# print(str7[0:-1:2]) # str7[start:stop:step]
# print(str7[::-1]) # itrisatel'nyi shag nachinaet chtenie stroki s konsa

# print(str7.find('ell')) # 1 - poisk indeks podstroki v stroke
# print(str7.index('w'))  # 6 
# print('*'.join(['hello', 'world', 'buy'])) # soedonyaet peredannyi spisok strok po ukazannoi stroke
# str8 = 'dhgbhjf'
# print(str8)
# print(str8.strip('*')) # ubiraet ukazannyi simvol c stroke s dvuz storon, esli ne ukazan simvol, po umolchaniyu - probel
# str8.lstrip() # - ubiraet probely sleva
# str8.rstrip() # - ubiraet probely sprava

# print(str8.isalpha())


'''metody proverki'''

string = 'My test string 123'
# print(string.isdigit)
string.isalpha() #False
string.isalnum() #False
string.isspace() #False
string.islower() #False
string.isupper() #False
string.endswith('123') #True
string.startswith('My') #True

num1 = 10
num2 = 20
num1 > num2 #False
num1 < num2 # True
num1 == num2 #False
num1 != num2 #True - neravenstvo
num1 <= num2 #True
num1 >= num2 #False

# str1 = 'apple'
# str2 = 'hello'
# print(str1 > str2) 
ord('a') # 97
chr(97)  # 'a'
# ASCII table

# a = 'absd'
# b = 'absed'
# sorted(a)
# sorted(b) 

'''formatirovanie strok'''

stat = 'privet , Farhad!'
# name = input()
# place = input()

# %
# str5 = 'ptivet, %s!' % name
# print(str5)

# str6 = 'privet, {}'.format(name)
# print(str6)

# str7 = f'hello {name}, welcome to {place}'
# print(str7)

# formatirovaniye strok - eto podstanovka peremennyx v stroku, sozdaniye dinamicheskoi stroki 

# a = 'I\'m student'
# b = 'idet bychok kachaetsya,\n\tVzdyxaet na xodu'
# print(b)
#  \n - newline
# \t - tabular

str8 = r'this is string\n\t\n' #r - raw
# print(str8)
windows_path = 'Users\Documents\\new_folders'
# print(windows_path) 

# str9 = 'hello world'
# str10 = 'ell'
# print(str10 in str9)


string = 'hello'
# print(dir(string))
# dir(obj) - функция возвращает список методов доступных переданному обьекту

