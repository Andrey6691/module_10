from time import sleep
import threading
import time


def write_words(word_count, file_name):
    for i in range(word_count):
        with open (file_name, 'a', encoding='utf-8') as file:
            file.write(f'Какое-то слово №  {i+1}\n')
            sleep(0.1)
    print (f'Завершилась запись в файл {file_name}')



started_at = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
ended_at = time.time()
elapsed = round(ended_at - started_at, 4)
print(f'Работа потоков: {elapsed} секунд')

started_at = time.time()
thread1 = threading.Thread(target=write_words, args = (10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args = (30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args = (200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args = (100, 'example8.txt'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

ended_at = time.time()
elapsed = round(ended_at - started_at, 4)
print(f'Работа потоков: {elapsed} секунд')



