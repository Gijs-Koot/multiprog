import threading
import time

ADD_LOCK = threading.Lock()

class Counter:

    count = 1

    def increase(self, i):
        
        print(f"Hi from thread {i}!")

        with ADD_LOCK:   # acquire the lock
            print(f"Thread {i} has acquired the lock!")
            sum = self.count
            time.sleep(0.01)
            self.count = sum + 1
            print(f"Thread {i} releases the lock")
        # lock is released


if __name__ == "__main__":

    counter = Counter()

    workers = []
    for i in range(100):
        
        worker = threading.Thread(target=counter.increase, args=(i,))
        worker.start()
        workers.append(worker)

    for worker in workers:
        worker.join()

    print(counter.count)

