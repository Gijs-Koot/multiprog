from celery_task import do_hard_work

for i in range(100):
    
    print(f"Starting task {i}")
    do_hard_work.delay(i)