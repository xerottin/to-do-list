from celery import Celery

celery_app = Celery(
    'worker',
    broker='amqp://localhost',
    backend='rpc://'
)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='Europe/Moscow',
    enable_utc=True,
)
