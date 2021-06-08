from celery.task.schedules import crontab
from celery.decorators import periodic_task


@periodic_task(run_every=(crontab(minute='*/15')), name="some_task", ignore_result=True)
def some_task():
    print('im a freaking task')
