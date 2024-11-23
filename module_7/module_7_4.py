team1_num = 5;
team2_num = 6
score_1 = 42;
score_2 = 40
team1_time = 1894.4934;
team2_time = 2012.00001

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

print("В команде Мастера кода участников:%d!" % team1_num)
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))
print("Команда Волшебники данных решила задач: {0} !".format(score_1))
print("Команда Волшебники данных решила задачи за: {0:.1f} !".format(team1_time))
print(f"Команды решили {team1_num} и {team2_num} задач.")
print(f"Результат битвы: {result}")
print(
    f"Сегодня было решено {team1_num + team2_num} задач, в среднем по {(team1_time + team2_time) / (team2_num + team1_num):.1f} секунды на задачу!.")

# просто развлекся
lst = [12.0, 65.000001, 0.000001, -1, 0.23]  # список произвольной длины в табличке
print("табличко через %:")
print("+" + "---------+" * len(lst))
print(("|" + ("%9.2g|" * len(lst))) % tuple(lst))
print("+" + "---------+" * len(lst))
print(("|" + ("%9.2e|" * len(lst))) % tuple(lst))
print("+" + "---------+" * len(lst))
print(("|" + ("%9.2f|" * len(lst))) % tuple(lst))
print("+" + "---------+" * len(lst))

print("табличко через format:")
print("+" + "---------+" * len(lst))
print("|" + "".join(["{0:9.2g}|".format(x) for x in lst]))
print("+" + "---------+" * len(lst))
print("|" + "".join(map(lambda x: "{:9.2e}|".format(x), lst)))
print("+" + "---------+" * len(lst))
print("|" + "".join(  [ "{"+ str(i) +":9.2f}|" for i in range(len(lst))]  ).format(*tuple(lst)))
print("+" + "---------+" * len(lst))

print("табличко через f-string:")
print("+" + "---------+" * len(lst))
print("|" + "".join([f"{x:9.2g}|" for x  in lst]))
print("+" + "---------+" * len(lst))
print("|" + "".join(map(lambda x: f"{x:9.2e}|", lst)))
print("+" + "---------+" * len(lst))
print("|" + "".join([f"{i:9.2g}|" for i in range(len(lst))]))
print("+" + "---------+" * len(lst))
