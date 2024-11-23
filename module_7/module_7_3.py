import os
import re


class WordsFinder():
    __seps = [',', '.', '=', '!', '?', ';', ':', ' - ']

    def __init__(self, *filenames: str):
        self.__data = dict[str, list[str]]()
        self.__filenames = filenames
        self.get_all_words()

    def get_all_words(self) -> dict[str, list[str]]:
        self.__data = dict[str, list[str]]()
        for fname in self.__filenames:
            with open(fname, encoding='utf-8') as f:
                txt = f.read()
                for s in self.__seps:
                    txt=txt.replace(s,' ')
                words=txt.split()
                # удоляем пробелы в словах. приводим в lower()?
                words = [s.strip().lower() for s in words]
                self.__data[fname] = words
        return self.__data

    def find(self, word: str) -> dict[str, int]:
        # self.get_all_words() - не вижу смысла делать  это каждый раз
        w = word.strip().lower()
        res = dict[str, int]()
        for fname, wds in self.__data.items():
            for i in range(len(wds)):
                if w == wds[i]:
                    res[fname] = i + 1
                    break
        return res

    def count(self, word: str) -> dict[str, int]:
        # self.get_all_words() - не вижу смысла делать  это каждый раз
        w = word.strip().lower()
        res = dict[str, int]()
        for fname, wds in self.__data.items():
            c = 0
            for i in range(len(wds)):
                if w == wds[i]:
                    c += 1
            res[fname] = c
        return res


path = '7_3_files'
os.chdir(path)

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
print("==============================================")
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
print("==============================================")
finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))
print("==============================================")
finder1 = WordsFinder('Rudyard Kipling - If.txt',)
print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))
print("==============================================")
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
