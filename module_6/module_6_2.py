class Vehicle:
    _COLOR_VARIANTS: list = ['red', 'blue', 'white', 'black', 'rainbow', 'golden']

    def __init__(self, owner: str, model: str, color, engine_power: int):
        self.owner: str = owner
        self.__model: str = model
        self.__engine_power: int = engine_power
        self.__color: str = color  # если не из _COLOR_VARIANTS то raise ?

    def get_model(self) -> str:
        return f"Модель: {self.__model}"

    def get_horsepower(self) -> str:
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self) -> str:
        return f"Цвет: {self.__color}"

    def print_info(self) -> None:
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, newcolor: str) -> None:
        if newcolor.lower() in Vehicle._COLOR_VARIANTS:
            self.__color = newcolor
        else:
            print(f"Нельзя изменить цвет на {newcolor}")


class Sedan(Vehicle):
    _PASSENGER_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
