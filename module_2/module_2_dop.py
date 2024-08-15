def get_pairs(n):
    pairs = []
    for x in range(1, n):
        # for y in range(x, n): -- должно быть по условию вот так,
        # но в примере у вас почему-то нет пар одинаковых чисел.
        # например почему для 6 мы пропускаем 3+3 ?
        for y in range(x + 1, n):
            if n % (x + y) == 0:
                pairs += [x, y]
    return pairs


# может это в строку надо было переводить. а не печатать? или составить длинный-длинный int?
def print_pass(nums):
    for x in nums:
        print(x, sep='', end='')

# так проще проверять:
def print_fancy(nums):
    for i in range(0, len(nums), 2):
        print(nums[i], '+', nums[i + 1], sep='', end=' ')


for n in range(3, 21):
    print(n, '-', end=' ')
    print_pass(get_pairs(n))
    print('')
print('')
for n in range(3, 21):
    print(n, '-', end=' ')
    print_fancy(get_pairs(n))
    print('')
