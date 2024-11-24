import multiprocessing
import time
from datetime import  timedelta

def read_info(name) -> None:
    all_data = []
    with open(name) as f:
        while True:
            s = f.readline()
            if len(s) > 0:
                all_data.append(s)
            else:
                break


prefix = './10_5_files/'
filenames = [prefix + 'file 1.txt', prefix + 'file 2.txt', prefix + 'file 3.txt', prefix + 'file 4.txt']



if __name__ == '__main__':
    t0 = time.perf_counter()
    for fname in filenames:
        read_info(fname)
    t1 = time.perf_counter()
    print(f"single-process:  {timedelta(seconds=t1 - t0)}")


    t0=time.perf_counter()
    with multiprocessing.Pool(len(filenames)) as p:
        p.map(read_info, filenames)
    t1=time.perf_counter()
    print(f"multi-process:  {timedelta(seconds=t1-t0)}")
