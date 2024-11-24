first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_res = (len(z[0]) - len(z[1]) for z in zip(first, second) if len(z[0]) != len(z[1]))
second_res = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_res))
print(list(second_res))
