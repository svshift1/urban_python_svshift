from collections.abc import Iterable


# извините. изучаю новое для себя -- typehints.


def count_calls() -> int:
    global calls
    calls += 1
    return calls


def string_info(s: str) -> tuple:
    count_calls()
    return len(s), s.upper(), s.lower()


def is_contains(s: str, lst: Iterable) -> bool:
    count_calls()
    for x in lst:
        if issubclass(type(x), str):
            # в документации говорится что casefold в контексте case_insensitive сравнения
            # универсальнее upper или lower. в пример приводятся европейские языки
            # типа греческого или немецкого где разным строчным буквам может соответсвовать
            # одна заглавная или сдвоенная
            if s.casefold() == x.casefold():
                return True
    return False


calls: int = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
