from collections.abc import Sequence, Iterable, Sized
from functools import reduce
import math

# не обращайте внимание. я просто изучаю что это такое.
type Color = Sequence[int, int, int]


class Figure(Sized):  #иначе len(self) не работает,  а только  self.__len__()    ¯\_(ツ)_/¯
    sides_count = 0

    def __init__(self, color: Color, sides: (Sequence[int | float]), filled: bool = False):
        if not self.__is_valid_sides(sides):
            self.__sides = [1] * self.sides_count
        else:
            self.__sides: list[int | float] = list(sides)  # я ради этого и экспериментирую с типами и подсказами
        if self.__is_valid_color(color):
            self.__color = tuple(color)
        else:
            self.__color=(-1,-1,-1)

        self.filled = filled  # не используется. не понятно куда его в конструктор совать

    def get_color(self):
        return list(self.__color)

    @staticmethod
    def __is_valid_color(c: Color) -> bool:
        if len(c) != 3:
            return False
        for n in c:
            if n < 0 or n > 255:
                return False
        return True

    def set_color(self, *c) -> None:
        if len(c) == 3:
            if self.__is_valid_color(c):
                self.__color = tuple(c)
        elif len(c) == 1 and len(c[0]) == 3:
            if self.__is_valid_color(c[0]):
                self.__color = tuple(c[0])

    # useage:   self.__is_valid_sides(a,b,c) or self.__is_valid_sides([a,b,c])
    def __is_valid_sides(self, *sides) -> bool:
        if len(sides) == 1 and isinstance(sides[0], Iterable):
            # если одним первым аргументом передали список
            # прошлый раз использовал проверку hasattr(obj, '__iter__'):
            if len(sides[0]) == self.sides_count:
                # извините, просто проверяю как это тут работает
                return reduce(lambda a, b: a and (0 <= b), sides[0], True)
        else:
            if len(sides) == self.sides_count:
                # извините, просто проверяю как это тут работает
                return reduce(lambda a, b: a and (0 <= b), sides, True)
        return False

    def __len__(self) -> float:
        return sum(self.__sides)

    # вот! подсказка типа результата помогла мне оформить все преобразования в конструкторе!
    def get_sides(self) -> list[int | float]:
        return self.__sides

    def set_sides(self, *sides) -> None:
        if not self.__is_valid_sides(sides):
            return
        # все проверки прошли
        if len(sides) == 1 and isinstance(sides[0], Iterable):
            self.__sides = sides[0]
        else:
            self.__sides = sides

    def __str__(self):
        return f"{type(self).__name__}(sides:{self.__sides}, color:{self.__color})"


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: Color, *sides):
        super().__init__(color, sides, False)
        # из описания задачи не понятно куда filled девать
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return self.__radius * 2 * math.pi

    def set_sides(self, *sides) -> None:
        super().set_sides(*sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: Color, *sides):
        super().__init__(color, sides, False)

    def get_square(self) -> float:
        p = 0.5 * len(self)  # см коммент в Figure
        a, b, c = self.get_sides()
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    # Cube((r,g,b), A) -- правильно
    # Cube((r,g,b), A, B, ...) -- не правильно
    # Cube([r, g, b], [A]) -- правильно
    # Cube((r, g, b), [A, B, ...]) -- не правильно
    def __init__(self, color: Color, *sides):
        x = 1
        if len(sides) == 1:
            if isinstance(sides[0], (int, float)):
                x = sides[0]
            elif isinstance(sides[0], Sequence) and len(sides[0][0]) == 1:
                x = sides[0][0]
        super().__init__(color, [x] * 12, False)

    def get_volume(self):
        return self.get_sides()[0] ** 3

    def get_square(self):
        return (self.get_sides()[0] ** 2) * 6

    def set_sides(self, *sides) -> None:
        if len(sides) == 1:
            if isinstance(sides[0], Iterable) and len(sides[0]) == 1:
                super().set_sides([sides[0][0]] * 12)
            else:
                super().set_sides([sides[0]] * 12)


print('== код для проверки ========')
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
print('== код для доп проверки ========')
circle1.set_sides(2,3)
print(circle1)  # ничего измениться не должно
t2=Triangle((200, 200, 100), 10, 6)
print(t2) # [1,1,1]
t3=Triangle((200, 200, 100), 3,4,5)
print(f"{t3}, sq={t3.get_square()}") # Triangle(sides:[3, 4, 5], color:(200, 200, 100)), sq=6.0
print(Circle((600, 200, 100), 10, 15, 6))  # Circle(sides:[1], color:(-1, -1, -1))
print(Cube((200, 200, 100), 9, 12)) # Cube(sides:[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], color:(200, 200, 100))

