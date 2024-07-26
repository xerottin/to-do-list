from celery import Celery
from config import RABBITMQ_BROKER_URL

celery_app = Celery('worker', broker=RABBITMQ_BROKER_URL)


@celery_app.task
def add(x, y):
    return x + y
