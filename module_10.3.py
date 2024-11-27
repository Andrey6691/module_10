import threading
import time
from random import randint

class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        self.lock.acquire()
        for i in range(100):
            x = randint(50, 500)
            self.balance += x
            time.sleep(0.05)
            print(f'Пополнение: {x}, Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()


    def take(self):
        self.lock.acquire()
        n=100
        while n != 0:
            x = randint(50, 500)
            print(f'Запрос на {x}')
            if x <= self.balance:
                self.balance -= x
                n -=1
                print(f'Снятие: {x}. Баланс:{self.balance}')

                 # self.lock.release()
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')





