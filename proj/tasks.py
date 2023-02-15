from .celery import celery

@celery.task
def add(x, y):
    return x + y

@celery.task
def mul(x, y):
    return x * y


@celery.task
def xsum(numbers):
    return sum(numbers)


from proj.tasks import add
res = add.delay(2, 2)
print(res)