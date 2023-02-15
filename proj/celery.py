from celery import Celery

celery = Celery('proj',
             broker='pyamqp://',
             backend='redis://localhost',
             include=['proj.tasks'])
             
# Optional configuration, see the application user guide.
celery.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    celery.start()