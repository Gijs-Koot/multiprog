import celery
import logging
import time

url = f"sqs://"

celery_app = celery.Celery(
    'tutorial',
    broker=url,
    broker_transport_option={'region': 'eu-west-1'}
)

@celery_app.task
def do_hard_work(identifier):

    print(f"I am working on {identifier}!")
    time.sleep(3)
    print(f"Done working on {identifier}!")
    