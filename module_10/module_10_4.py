import queue
import random
from queue import Queue
import threading
import time


class Table:

    def __init__(self, number: int):
        self.number = number
        self.guest = None


class Guest(threading.Thread):

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:

    def __init__(self, *tables: Table):
        self.tables: list[Table] = list(tables)
        self.queue = queue.Queue()

    def guest_arrival(self, *guests: Guest):
        # рассадка
        for g in guests:
            t: Table = self.__first_free_table()
            if t is None:
                self.queue.put(g)
                print(f"{g.name} соизволили ожидать в очереди")  # и никаких гендерных окончаний )
            else:
                t.guest = g
                print(f"{g.name} усажены за стол №{t.number}")
                g.start()  # запустили поток

    def serve_guests(self):
        while True:
            for t in self.tables:
                if t.guest is not None and not t.guest.is_alive():
                    print(f"{t.guest.name} закончили трапезничать и соизволили восвояси")
                    t.guest = None
                    print(f"Стол №{t.number} освободился")
                elif t.guest is None and not self.queue.empty():
                    t.guest = self.queue.get()
                    print(f"{t.guest.name} соизволили дождаться и занять столик №{t.number}")
                    t.guest.start()
            if all(t.guest is None for t in self.tables) and self.queue.empty():
                break
            time.sleep(0.01)
        print("никто не ушел обиженным")

    # вернуть первый свободный столик
    def __first_free_table(self) -> (Table, None):
        for t in self.tables:
            if t.guest is None:
                return t
        return None


# noms = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
#         'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

noms = ['Émilie', 'Julien', 'Claire', 'Antoine', 'Camille', 'Laurent', 'Chloé', 'Nicolas', 'Sophie' 'Maxime',
        'Juliette', 'Philippe', 'Manon', 'Thomas', 'Lucie', 'Hugo', 'Pauline', 'Alexandre', 'Léa', 'Baptiste']

invites = [Guest(n) for n in noms]

n_tables = 5
tables = [Table(n) for n in range(1, n_tables + 1)]

le_cafe = Cafe(*tables)
le_cafe.guest_arrival(*invites)
le_cafe.serve_guests()
