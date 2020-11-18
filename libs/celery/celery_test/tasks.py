from celery import Celery 

app = Celery('tasks', broker='redis://11.160.137.194:16379/0', backend='redis://11.160.137.194:16379/0')

@app.task
def add(x, y):
    return x + y
