

class House:
    houses_history = []

    def __new__(cls, *args, **kwargs) :
        # в явном виде вызвать родительский __new__ !!!
        # без этого ломается механизм подсчета ссылок )))
        # и не изменятся унаследованные статические поля
        class_instance = super().__new__(cls, args, kwargs) # ввопрос в к-ве подмножества args
        if 'name' in kwargs:
            #print("kwargs")
            cls.houses_history.append(str(kwargs['name']))
        else:
            #print("args")
            cls.houses_history.append(str(args[0]))
        return class_instance

    def __init__(self, name: str, floors: int):
        self.name: str = name
        self.number_of_floors: int = floors  # проверки на отрицательные этажи пока не предусмотрены?

    def __del__(self) -> None:
         print(f"{self.name} снесён, но он останется в истории")

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
        # строго говоря его даже не надо через __add__ реализовывать.
        # если не определить, то оно по дефолту будет через __add__ реализовано
        # но я привык наоборот __add__ писать через __iadd__ -- привычка из C++
        if isinstance(other, House):
            self.number_of_floors += other.number_of_floors
        elif isinstance(other, int):
            self.number_of_floors += other
        else:
            raise "не положено складывать с таким"
        return self


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House(floors=20, name='ЖК Акация')
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)


del h2
del h3


print(House.houses_history)
