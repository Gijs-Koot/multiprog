import threading
import time
import logging

# EXERCISE: start ten threads that all run this program at the same time

def wait(i: int):
    time.sleep(1)
    print(f"waiting {i}")

if __name__ == "__main__":

    worker = threading.Thread(target=wait, args=(42, ), daemon=True)
    worker.start()
    worker.join()    

    print("Bye!")

    