import time
from queue import Queue
import threading
from random import randint
from threading import Thread

class Table:

    def __init__ (self, number):
        self.guest = None
        self.number = number

class Guest(Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run (self):
        time.sleep(randint(3, 10))

class Cafe:

    def __init__ (self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f'{guest.name} сел(-а) за стол {table.number}')
                    table.guest.start()
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while (not self.queue.empty()) or(not (t.guest for t in self.tables)):
            for table in self.tables:
                if (not self.queue.empty()) and (table.guest is None):
                    table.guest = self.queue.get()
                    print(f'{Guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()
                if (not table.guest is None) and (table.guest.is_alive()):
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер{table.number} свободен')
                    table.guest = None


tables = [Table(number) for number in range(1, 6)]
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()