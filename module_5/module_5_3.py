class House:
    def __init__(self, name: str, floors: int):
        self.name: str = name
        self.number_of_floors: int = floors  # проверки на отрицательные этажи пока не предусмотрены?

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

    def __eq__(self, other: 'House') -> bool:
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return False

    def __ge__(self, other: 'House') -> bool:
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return False

    def __gt__(self, other: 'House') -> bool:
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return False

    def __le__(self, other: 'House') -> bool:
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return False

    def __lt__(self, other: 'House') -> bool:
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return False

    # # видимо предполагалось что-то такое:
    # def __add__(self, other: ('House', int)) -> 'House':
    #     if isinstance(other, House):
    #         return House(self.name, self.number_of_floors + other.number_of_floors)
    #     elif isinstance(other, int):
    #         return House(self.name, self.number_of_floors + other)
    #     else:
    #         raise "не положено складывать с таким"

    def __add__(self, other: ('House', int)) -> 'House':
        res = House(self.name, self.number_of_floors)
        res += other
        return res

    def __radd__(self, other: ('House', int)) -> 'House':
        return self + other

    def __iadd__(self, other: ('House', int)) -> 'House':
        # строго говоря его даже недо через __add__ реализовывать.
        # если не определить, то оно по дефолту будет через __add__ реализовано
        # я привык наоборот __add__ писать через __iadd__ -- привычка из C++
        if isinstance(other, House):
            self.number_of_floors += other.number_of_floors
        elif isinstance(other, int):
            self.number_of_floors += other
        else:
            raise "не положено складывать с таким"
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
