#coding=utf-8
from celery import Celery 
from celery.bin import worker as celery_worker
import celeryconfig 

broker = 'redis://11.160.137.194:16379/0'
backend = 'redis://11.160.137.194:16379/0'
app = Celery('celery_test', backend=backend, broker= broker)
app.config_from_object(celeryconfig)

@app.task
def mytask0(task_name):
    print("task0: %s" % task_name)
    return task_name

@app.task
def mytask1(task_name):
    print("task1: %s" % task_name)
    return task_name

def worker_start():
    worker = celery_worker.worker(app=app)
    worker.run(broker=broker, 
               concurrency=4, 
               traceback=False, 
               loglevel='INFO')

if __name__ == '__main__':
    worker_start()
