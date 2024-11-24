import random
import threading
import time


class Bank:

    def __init__(self, balance: int = 0):
        self.balance = balance
        self.lock = threading.Lock()
        # синхронизовать сами операции снятия и получения,
        # чтобы избежать каши на экране
        # типа внесение и снятие через одно окно
        self.globallock = threading.Lock()

    def deposit(self):
        for i in range(100):
            self.globallock.acquire()  #заняли кассу
            amount = random.randint(50, 500)
            self.balance += amount
            print(f"Пополнение {amount}. Баланс: {self.balance}")
            if self.balance >= 50 and self.lock.locked():
                self.lock.release()
            self.globallock.release()  #освободили кассу
            time.sleep(0.001)
            # time.sleep(0.0001*random.randint(5,10))

    def withdraw(self):
        for i in range(100):
            self.globallock.acquire()  #заняли кассу
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")
            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие {amount}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                if not self.lock.locked():
                    self.lock.acquire()
            self.globallock.release()  #освободили кассу
            time.sleep(0.001)
            # time.sleep(0.0001*random.randint(5,10))
        # чтобы не висло в конце, когда останавливаемся на низком балансе
        if self.lock.locked():
            self.lock.release()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.withdraw, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
