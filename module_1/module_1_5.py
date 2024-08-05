#1. В проекте, где вы решаете домашние задания, создайте модуль 'module_1_5.py' и напишите весь код в нём.

#2. Задайте переменные разных типов данных:
#  - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
#  - Выполните операции вывода кортежа immutable_var на экран.

immutable_var=(1,"два",3.0, True)
print("immutable ", type(immutable_var).__name__,':',immutable_var)

# 3. Изменение значений переменных:
#   - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.

try :
    immutable_var[0]="two";
except Exception as e:
    print("тюплы не поддерживают изменение: Excedption "+str(type(e))+":"+str(e))

# 4. Создание изменяемых структур данных:
#   - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
#   - Измените элементы списка mutable_list.
#   - Выведите на экран измененный список mutable_list.

mutable_list=[1,"два",3.0, True]
#another_list=mutable_list # -- ссылка на тот же объект
mutable_list[1]="two" # значение поменятеся и в another_list[1]
print('mutable ',type(mutable_list).__name__,':',mutable_list);
#print('another mutable ',type(another_list).__name__,':',another_list);