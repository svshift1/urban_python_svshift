import threading
import time


mutex=threading.Lock()
class Knight(threading.Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        mutex.acquire()  # эээ...  мне не нравится что у меня на консоли каша из строк, я в курсе что Lock  исучают дальше
        print(f"{self.name} на нас напали!")
        mutex.release()
        t = 0;
        enemies = 100
        while enemies > 0:
            enemies -= self.power
            if enemies<0:
                enemies=0
            t+=1
            time.sleep(1)
            mutex.acquire()
            print(f"{self.name} сражается {t} день(дня)..., осталось {enemies} врагов")
            mutex.release()
        mutex.acquire()
        print(f"{self.name} одержал победу спустя {t} дней(дня)!")
        mutex.release()


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()