from celery import Celery
from celery.schedules import crontab

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def greet(name):
    print(f"Hello, {name}!")

@app.task
def add(x, y):
    print(f"The sum of {x} and {y} is {x + y}")

# Celery Beat schedule
app.conf.beat_schedule = {
    'say-hello-every-1-second': {
        'task': 'tasks.greet',
        'schedule': 1.0,  
        'args': ('Rafi',)
    },

    'add-numbers-every-1-seconds': {
        'task': 'tasks.add',
        'schedule': 1.0,  
        'args': (10, 20)
    },
}
app.conf.timezone = 'Asia/Dhaka'