import requests
import time
from concurrent.futures import ThreadPoolExecutor

def check_url(url: str) -> int:

    response = requests.get(url)
    # raise Exception("NOOO!")
    return response.status_code

if __name__ == "__main__":

    urls = ["http://www.google.nl", "http://www.nu.nl", "http://www.nos.nl", "http://docs.python.org"]

    with ThreadPoolExecutor(max_workers=4) as pool:
        # results = pool.map(check_url, urls)
        results = list()
        for url in urls:
            results.append(pool.submit(check_url, url))
            results[-1].add_done_callback(lambda res: print(res.result()))