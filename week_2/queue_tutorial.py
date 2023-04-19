from queue import Queue, Empty
import threading
import requests
import time
import datetime

num_threads = 5

work_queue = Queue()

urls = ["http://octo.nu", "http://google.nl", "http://ns.nl", "http://nu.nl", "http://nos.nl"]

for url in urls:
    work_queue.put(url)

# we have a queue with 5 items

def actual_work(url):
    response = requests.get(url)
    print(f"{url} - {response.status_code}")

def work_the_queue():
    while True:
        try:
            item = work_queue.get(timeout=1)
            actual_work(item)
        except Empty:
            print("Done!")
            return

for i in range(num_threads):
    threading.Thread(target=work_the_queue).start()


    
print("All threads done")