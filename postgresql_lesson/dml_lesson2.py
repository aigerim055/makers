'''
SELECT - выборка данных
SELECT * FROM table_name; - выборка всех полей
SELECT column_name FROM table_name; - выборка указанных полей

WHERE - фильтрация данных 
SELECT * FROM table_name WHERE condition;


операторы сравнения:
> 
< 
= - сравнение
<=
>=
!=  or <>
AND - и
OR -или
IN - в
BETWEEN - между
LIKE - подходит ли под шаблон(с учетом регистра)
ILIKE - без учета регистра

'%a%' - в слове есть буква 'a'
'a%' - слово начинается с буквы 'a'
'____' -  количество андерскоров опр кол символов


IS NULL -  проверка на пустое значение 
NOT - отрицание условия

LIMIT - установка количества выдамаемых записей
ORDER BY - сортировка по полю
GROUP BY - группировка по опр столбцу
DESC - по убыванию, ASC - по возрастанию(по умолчанию)



UPDATE-обновление данных
UPDATE table_name SET column_name = value, column_name2 = value2 WHERE condition;

DELETE-удаление данных
DELETE FROM table_name; - очистка всей таблицф
DELETE FROM table_name WHERE condition; -очистка данных подходящих под условие

INSERT INTO- добавление данных
INSERT INTO table_name (column_names) VALUES (values_for_columns);




функции в PostgreSQL

агрегационные функции:
COUNT() - функиця для счета количества вхождений
AVG()- поиск среднего значения
MAX() - поиск  максимального значения
MIN() - поиск минимального значения
SUM() - поиск результата сложения всех значений

ROUND() - округление значений с плавающей точкой
|| - конкатенация
CASE WHEN - подстановка знаений в зависимости от условий
SELECT column_name CASE WHEN conition THEN value1 ELSE vaue2 END FROM table_name;



JOIN - связи между таблицами
FULL JOIN- соед все данные
LEFT JOIN - соед из левой таблицы
RIGHT JOIN - соед из правой таблицы
INNER JOIN - соед только тех данных, которые имеют пересечение

SELECT * FROM person RIGTH JOIN pets;

'''