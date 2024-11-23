import os.path


class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self) -> str:
        return f"{self.name}, {self.weight}, {self.category}"

    # попробую без нее
    # def __eq__(self, other) ->bool:
    #     return self.name==other.name


class Shop:

    def __init__(self, filename: str = 'products.txt'):
        self.__filename: str = filename
        self.__products: list[Product] = []
        if not os.path.isfile(filename):
            # создать путой файл
            f=open(filename,'w')
            f.close()
        else:
            self.get_products()

    def add(self, *products: Product) -> None:  # типа тогда products ожидается как tuple[Product]
        self.get_products()
        for it in products:
            if any(p.name.lower() == it.name.lower() for p in self.__products):
                print(f"Продукт {it.name} уже есть в магазине")
            else:
                self.__products.append(it)
                f = open(self.__filename, mode="a", encoding="cp1251", errors='replace')
                f.write(str(it) + '\n')
                f.close()

    def get_products(self) -> str:
        f = open(self.__filename, mode="r", encoding="cp1251", errors='replace')
        # lines = f.readlines() # так \n останутся в овощах
        lines = map(lambda x: x.rstrip('\n'), f.readlines())
        f.close()
        self.__products = []
        for s in lines:
            params = s.split(', ')
            self.__products.append(Product(params[0], float(params[1]), params[2]))
        res = '\n'.join(map(str, self.__products))
        return res

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
# формально Potato уже есть в магазине. пример работы программы приведенный в задании некорректен
# в задании сказано сравнивать только по названию
# здесь он обязан сказать что картоха уже есть.
p3 = Product('POTATO', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
