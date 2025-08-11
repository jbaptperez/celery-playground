from celery import Celery

app = Celery()
app.config_from_object(
    obj="celery-playground.celeryconfig",
    silent=False,
    force=True,
)
app.autodiscover_tasks(
    packages=["celery-playground.workflow"], related_name="tasks", force=True
)
