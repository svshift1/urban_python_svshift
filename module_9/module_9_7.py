from collections.abc import Callable


def isprime(func: Callable) -> Callable:
    def check_prime(*args):
        res = func(*args)
        if not isinstance(res, int):
            raise TypeError('Результат должен быть целым')
        if res <= 0:
            raise ValueError('Число должно быть натуральным')
        if res == 1:
            print("Это единица")
        elif res > 1 and not any(res % i == 0 for i in range(2, res // 2)):
            print("Простое")
        else:
            print("Составное")
        return res

    return check_prime


@isprime
def sum_three(a: int, b: int, c: int) -> int:
    return a + b + c


print(sum_three(20, 20, 3))
print(sum_three(20, 20, 4))
