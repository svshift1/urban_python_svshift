def get_multiplied_digits(num):
    n = int(num)
    s = str(n)  # убрали ведущие нули если были в num если это была строка
    if int(s) == 0:
        # последний ноль(и)
        return 1
    elif len(s) == 1 and int(s) != 0:
        # последний символ числа не ноль
        return int(s[0])
    else:
        return int(s[0]) * get_multiplied_digits(int(s[1:]))


result = get_multiplied_digits(40203)
print(result)

result = get_multiplied_digits(402030)
print(result)

result = get_multiplied_digits('00402030')
print(result)
