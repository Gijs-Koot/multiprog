import multiprocessing
import time

from concurrent.futures.process import ProcessPoolExecutor

counter = 1

def increase(i: int):

    global counter
    time.sleep(1)
    counter += 1 
    return counter

with ProcessPoolExecutor(max_workers=20) as pool:
    for count in pool.map(increase, range(100)):
        print(count)

print("Done!")
