import threading
import time
import multiprocessing
from multiprocessing import Pool

def read_info(name):
    file = open(name, 'r')
    all_data = []
    while True:
        line = file.readline()
        if not line:
            break
        all_data.append(line.strip())

'Линейный вызов'
filenames = [f'./file {number}.txt' for number in range(1, 5)]

started_at = time.time()
for i in filenames:
    name = i
    result = read_info(name)
ended_at = time.time()
elapsed = round(ended_at - started_at, 4)
print(f'Время линейной обработки: {elapsed} секунд')

# 'Многопроцессный вызов'
# if __name__ == '__main__':
#     start_time = time.time()
#     with Pool(4) as p:
#         names = ('file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt')
#         result = p.map(read_info, names)
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     print('Время многопроцессной обработки: ', elapsed_time)