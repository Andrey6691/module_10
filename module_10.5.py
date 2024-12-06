import threading
import time
import multiprocessing
from multiprocessing import Pool

def read_info(filenames):
    file = open(filenames, 'r')
    all_data = []
    while True:
        line = file.readline()
        if not line:
            break
        all_data.append(line.strip())


filenames = [f'./file {number}.txt' for number in range(1, 5)]


if __name__ == '__main__':

    # 'Линейный вызов'

    started_at = time.time()
    for i in filenames:
        name = i
        result = read_info(name)
    ended_at = time.time()
    elapsed = round(ended_at - started_at, 4)
    print(f'Время линейной обработки: {elapsed} секунд')

    # 'Многопроцессный вызов'

    start_time = time.time()
    with Pool(4) as p:
        result = p.map(read_info, filenames)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('Время многопроцессной обработки: ', elapsed_time)
