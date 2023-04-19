import queue
from pathlib import Path
import tempfile
import threading
from woco_core.connections.db_util import connection_from_config
from woco_core.config import Config
import logging
import boto3

logger = logging.getLogger(__name__)
logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s :%(message)s", level=logging.INFO)

download_path = Path(tempfile.gettempdir()) / "multithread"
download_path.mkdir(exist_ok=True)

connection = connection_from_config()
s3 = boto3.resource("s3")

sql = """
SELECT bucket, key FROM nl_data.sv_images LIMIT 100;
"""

with connection.cursor() as cursor:
    
    cursor.execute(sql)
    results = cursor.fetchall()

connection.close()

logger.info("Got the work!")

work_queue = queue.Queue()

# TODO create a queue here 
# TODO create workers that wait for things to appear on the queue

for res in results:
    
    bucket, key = res
    tgt = download_path / key.split("/")[-1]

    # TODO instead of doing the work here, put it on the queue
    # s3.Bucket(bucket).download_file(key, str(tgt))
    work_queue.put((bucket, key, tgt))

def save_to_file(bucket, key, tgt):
    logger.info(f"Saving {key}")
    s3.Bucket(bucket).download_file(key, str(tgt))
    logger.info(f"Saved {key}")

def work_the_queue():
    while True:
        try:
            bucket, key, tgt = work_queue.get(timeout=.05)
            save_to_file(bucket, key, tgt)
        except queue.Empty:
            return

threads = list()

for i in range(4):
    thread = threading.Thread(target=work_the_queue)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

logger.info("All done!")
