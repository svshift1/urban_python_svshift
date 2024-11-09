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

    def __len__(self) -> int:
        return self.number_of_floors

    def __str__(self) -> str:
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
