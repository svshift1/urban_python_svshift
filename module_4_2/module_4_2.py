
# имя test_function запускает автотесты вмето запуска скрипта
def get_function():
    def inner_function():
        print(" Я в области видимости функции get_function")

    print("test:")
    inner_function()


get_function()
# inner_function() # -- фиг вам
#get_function.inner_function() #-- тоже фигвам


