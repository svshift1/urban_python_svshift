from typing import Dict


def custom_write(filename: str, strings: list[str]) -> dict[tuple[int, int], str]:
    f = open(filename, 'w', encoding='utf-8')
    # res={}
    res = dict[tuple[int, int], str]()  # говорят typing.Dict устарел (
    for i in range(len(strings)):
        pos = f.tell()
        res[(i + 1, pos)] = strings[i]
        f.write(strings[i] + '\n')
    f.close()
    return res


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

