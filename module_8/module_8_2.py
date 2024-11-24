from collections.abc import Iterable, Sequence


def personal_sum(numbers: Iterable):
    s: float = 0
    incorrect_data: int = 0
    for it in numbers:
        try:
            s += it
        except TypeError as e:
            print(f"Некорректный тип данных для подсчёта суммы - {it}")  # в условии про это не сказано. это следует только из примера
            incorrect_data += 1
    return s, incorrect_data


def calculate_average(numbers: Sequence):
    try:
        s, incorrect_data = personal_sum(numbers)
        return s / (len(numbers)-incorrect_data)
    except TypeError as e:
        print('В numbers записан некорректный тип данных')
        return None
    except ZeroDivisionError as e:
        return 0

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать