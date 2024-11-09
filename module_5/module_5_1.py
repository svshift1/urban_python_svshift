class House:
    def __init__(self, name: str, floors: int):
        self.name: str = name
        self.number_of_floors: int = floors

    def go_to(self, new_floor: int) -> None:
        if 0 < new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('"Такого этажа не существует"')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
