class Animal:
    def __init__(self, name: str):
        self.alive: bool = True
        self.fed: bool = False
        self.name: str = name

    # поправьте меня - если у Mammal и Predator есть одинаковый метод eat
    # почему бы мне не вынести его сюда?
    def eat(self, food: 'Plant') -> None:
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Plant:
    edible: bool = False

    def __init__(self, name: str):
        self.name: str = name


class Mammal(Animal):

    def __init__(self, name: str):
        super().__init__(name)


class Predator(Animal):
    def __init__(self, name: str):
        super().__init__(name)


class Flower(Plant):

    def __init__(self, name: str):
        super().__init__(name)


class Fruit(Plant):
    edible: bool = True

    def __init__(self, name: str):
        super().__init__(name)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)