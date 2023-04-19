import threading
import time
import sys

def buggy():
    time.sleep(1)
    raise Exception("AAAHH!")

worker = threading.Thread(target=buggy)
worker.start()

print("Hello!")

