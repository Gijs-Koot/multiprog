# using threadpoolexecutor

from pathlib import Path
import tempfile
from typing import List
from woco_core.connections.db_util import connection_from_config
from woco_core.config import Config
from concurrent.futures import ThreadPoolExecutor
import boto3

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

# TODO create a threadpool here
# TODO create a function that takes a bucket and key name and returns the path where the file was saved
# TODO use pool.map to download all the images
# TODO print the result value from the function

work_items: List[tuple] = list()

for res in results:
    
    bucket, key = res
    tgt = download_path / key.split("/")[-1]

    work_items.append((bucket, key, tgt))

def save_to_file(bucket, key, tgt):
    s3.Bucket(bucket).download_file(key, str(tgt))

with ThreadPoolExecutor(max_workers=10) as pool:
    pool.map(save_to_file, work_items)




connection.close()