import threading
import time
from datetime import  timedelta


def write_words(n:int, filename: str) -> None:
    with open(filename,'w', encoding='utf-8') as f:
        for i in range(1, n+1):
            f.write(f"Кто-то что-то сказал №{i}")
            time.sleep(0.1)
    print(f"завершилось в {filename}")


t0=time.perf_counter()
write_words(0, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
t1=time.perf_counter()
print(f"Работа в 1 поток: {timedelta(seconds=t1-t0)}")
t0=time.perf_counter()
th1=threading.Thread( target=write_words, args=(10, 'example5.txt'))
th2=threading.Thread( target=write_words, args=(30, 'example6.txt'))
th3=threading.Thread( target=write_words, args=(200, 'example7.txt'))
th4=threading.Thread( target=write_words, args=(100, 'example8.txt'))
th1.start()
th2.start()
th3.start()
th4.start()
th1.join()
th2.join()
th3.join()
th4.join()
t1=time.perf_counter()
print(f"Работа в 4 потока: {timedelta(seconds=t1-t0)}")
