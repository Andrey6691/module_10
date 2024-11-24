import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        n = 0
        s = 100
        while s > 0:
            s = s - self.power
            n += 1
            print(f'{self.name} сражается {n}, осталось {s} воинов')
            time.sleep(1)
        else:
            print(f'{self.name} одержал победу спустя {n} дней')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
second_knight.start()
first_knight.start()
first_knight.join()
second_knight.join()
