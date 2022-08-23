'''     JSON    '''

# JavaScript Object Notation

human = {
    'name': 'aleksey',
    'age': 19,
    'is_married': True,
    'hobbies': ['music', 'football', 'games'],
    'job': None
}

import json

# JSON - формат обмена данными между языками, основанный на JavaScript

# Сериализация - перевод питон объектов на JSON-объекты

# json_str = json.dumps(human)
# print(json_str)

# Десериализация - перевод json-объекты в python-объекты

# json_human = '{"name": "Turar", "last_name": "Akimov", "job": null, "is_married": false}'
# python_human = json.loads(json_human)
# print(python_human)

p = [
    {
        'title': 'apple iphone 13', 
        'price': 222222
    },
    {
        'title': 'samsung galaxy s21',
        'price': 10000
    },
    {
        'title': 'Nokia 3310',
        'price': 12345
    }
]

# with open('products.json', 'w+') as file:
#     products = json.dumps(p, indent=4)
#     file.write(products)
#     file.seek(0)
#     python_products = json.load(file)
#     print(python_products)


# file = open('products2.json', 'w')
# json.dump(p, file, indent=4)
# file.close()
# print(file.closed)

