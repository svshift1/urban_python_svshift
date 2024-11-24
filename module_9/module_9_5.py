from collections.abc import Iterable

class StepValueError(ValueError):
    pass


class Iterator(Iterable):

    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        self.start = start+0  # ламерская проверка на не-число
        self.stop = stop+0
        self.step = step+0
        self.pointer = start

    def __iter__(self) -> 'Iterator':
        self.pointer=self.start
        return self

    def __next__(self):
        res=self.pointer
        self.pointer += self.step
        if self.step>0 and res>self.stop:
            raise StopIteration()
        if self.step<0 and res<self.stop:
            raise StopIteration()
        return res


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


# for i in iter2:
#     print(i, end=' ')
# print()
# for i in iter3:
#     print(i, end=' ')
# print()
# for i in iter4:
#     print(i, end=' ')
# print()
# for i in iter5:
#     print(i, end=' ')
# print()

print(*iter2, sep=', ')
print(*iter3, sep=', ')
print(*iter4, sep=', ')
print(list(iter5))  # <-- так лучше видно что последний список пустой
