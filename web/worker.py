from celery import Celery

app = Celery('tasks', broker='redis://redis:6379/0')

@app.task
def add_task(expression):
    try:
        return eval(expression)
    except Exception as e:
        return str(e)
