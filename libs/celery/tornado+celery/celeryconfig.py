# 这个文件里面包含着对celery的配置
from kombu import Queue
CELERY_DEFAULT_QUEUE = 'mytask0'
CELERY_QUEUES = (
    Queue('mytask0', routing_key = 'task.mytask0'),
    Queue('mytask1', routing_key = 'task.mytask1'),
)
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_DEFAULT_ROUTING_KEY = 'task.mytask0'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ROUTES = {
    'task.mytask0': {
        'queue': 'mytask0',
        'routing_key': 'task.mytask0',
    }, 
    'task.mytask1': {
        'queue': 'mytask0', 
        'routing_key': 'task.mytask1',
    },
}
