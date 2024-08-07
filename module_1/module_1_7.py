grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# ну так:
# res = dict(zip(students,[sum(x)/len(x) for x in grades]))

# или:
students = list(students)
res = {}
# нет, пять раз копировать одну строчку не буду
for i in range(len(students)):
    res[students[i]] = sum(grades[i]) / len(grades[i])
print(res)
