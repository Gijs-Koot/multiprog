from queue import Queue, Empty
import threading
import requests
import time
import datetime

num_threads = 2

work_queue = Queue()

urls = ["http://google.nl", "http://ns.nl", "http://nu.nl", "http://nos.nl", "http://octo.nu"]

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

for url in urls:
    work_queue.put(url)

threads = list()

for i in range(num_threads):
    thread = threading.Thread(target=work_the_queue)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("All threads done")