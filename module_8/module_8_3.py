

class IncorrectVinNumber(Exception):
    def __init__(self, msg: str):
        super().__init__()
        self.message=msg

    def __str__(self):
        return self.message


class IncorrectCarNumbers(Exception):

    def __init__(self, msg: str):
        super().__init__(msg)
        self.message=msg # зачем ?

    def __str__(self):
        return self.message


class Car:

    def __init__(self, model: str, vin: int, numbers: str):
        self.model: str = model
        if self.__is_valid_vin(vin):
            self.__vin=vin
        if self.__is_valid_numbers(numbers):
            self.__numbers=numbers

    @staticmethod  # PyCharm сам предложил
    def __is_valid_vin(vin: int) -> bool:
        if not isinstance(vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номера')
        if not 1000000 <= vin <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    @staticmethod  # PyCharm сам предложил
    def __is_valid_numbers(numbers: str) -> bool:
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if not len(numbers) == 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')