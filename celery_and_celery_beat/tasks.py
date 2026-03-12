from celery import Celery
from celery.schedules import crontab

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def greet(name):
    print(f"Hello, {name}!")

# Celery Beat schedule
app.conf.beat_schedule = {
    'say-hello-every-1-second': {
        'task': 'tasks.greet',
        'schedule': 1.0,  # every 1 second
        'args': ('Rafi',)
    },
}
app.conf.timezone = 'Asia/Dhaka'