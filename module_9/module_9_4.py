import random
from collections.abc import Callable

first = 'Мама мыла раму'
second = 'Рамена мало было'

# номер раз
first_res = list(map(lambda c1, c2: c1 == c2, first, second))


# номер два.
def get_advanced_writer(file_name: str) -> Callable:
    def write_everything(*data):
        with open(file_name,'w',encoding='utf-8') as f:
            for d in data:
                f.write(str(d)+'\n')

    return write_everything


# номер три
class MysticBall:

    def __init__(self, *words):
        self.words=words

    def __call__(self):
        return random.choice(self.words)

#результаты

print(first_res)

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# with open('example.txt', encoding='utf-8') as f:
#     for l in f:
#         print(l, end='')

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
