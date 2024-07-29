from .crud import create_task
from .celery_config import celery_app

from app import schemas
from app.database import SessionLocal


@celery_app.task
def add_task_to_db(task_data):
    db = SessionLocal()
    task = schemas.TaskCreate(**task_data)
    create_task(db=db, task=task)
    db.close()
