# 2. Работа со словарями:
#   - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
# Например: Имя(str)-Год рождения(int).

my_dict = {"Vendémiaire": 1,
           "Brumaire": 2,
           "Frimaire": 3,
           "Nivôse": 4,
           "Pluviôse": 5,
           "Ventôse": 6,
           "Germinal": 7,
           "Floréal": 8,
           "Prairial": 9,
           "Messidor": 10,
           "Thermidor": 11,
           "Fructidor": 12}

#   - Выведите на экран словарь my_dict.
print(my_dict)
#   - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
print(my_dict["Brumaire"])
try:
    print(my_dict["Fermidor"])
except Exception as e:
    print("такого ключа нет:", str(e))

#   - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
my_dict["heat month"]=11;
my_dict.update([("flower month",8)])

#  - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
print("\"Thermidor\":", my_dict.pop("Thermidor"))

#   - Выведите на экран словарь my_dict.
print(my_dict)

#
# 3. Работа с множествами:
#   - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.

my_set={ "one", "two", "three", "four", "one", "two"}

#   - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
print(my_set)

#   - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.update({"five","six"})
#   - Удалите один любой элемент из множества my_set.
if "one" in my_set:
    my_set.discard("one")
#   - Выведите на экран измененное множество my_set.
print(my_set)
