import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed: (int, float)):
        self._coords: list = [0, 0, 0]
        self.speed: int = speed

    def move(self, dx: (int, float), dy: (int, float), dz: (int, float)) -> None:
        self._coords[0] += dx * self.speed
        self._coords[1] += dy * self.speed
        self._coords[2] += dz * self.speed

    def get_coords(self) -> None:
        print(f"X: {self._coords[0]}, Y: {self._coords[1]}, Z: {self._coords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I am peacefull")
        else:
            print("Algaaa-a-ah! O_O")

    # в задании нет уточнения где именно должен определяться этот метод
    def speak(self):
        if self.sound is not None:
            print(self.sound)


class Bird(Animal):
    beak = True

    def __init__(self, speed: (int, float)):
        super().__init__(speed)

    def lay_eggs(self) -> None:
        n = random.randint(1, 4)
        if n == 1:
            print(f"Here is 1 egg for you")
        else:
            print(f"Here are {n} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed: (int, float)):
        super().__init__(speed)

    def dive_in(self, dz) -> None:
        self._coords[2] -= abs(dz) * self.speed / 2


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

    def __init__(self, speed: (int, float)):
        super().__init__(speed)


# он вам не DuckBill а Platypus !!!
class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    # почему в задании написано, что это доп атрибут? мы же его наследуем от Animal
    sound = "Click-click-click"

    def __init__(self, speed: (int, float)):
        super().__init__(speed)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_coords()
db.dive_in(6)
db.get_coords()

db.lay_eggs()
