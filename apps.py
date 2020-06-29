from django.apps import AppConfig
from django.conf import settings
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone
import logging
logger = logging.getLogger(__name__)

tz = timezone('Australia/Melbourne')
scheduler = BackgroundScheduler()

class DjangoApschedulerConfig(AppConfig):
    name = 'django_apscheduler'
    verbose_name = "Django APScheduler"

    def ready(self):
        from django_apscheduler.jobstores import DjangoJobStore, register_events
        scheduler.add_jobstore(DjangoJobStore(), 'default')
        logger.info("Django job store added to scheduler")
        register_events(scheduler)
        if settings.SCHEDULER_AUTOSTART:
            scheduler.start()
            logger.info("Scheduler started!")
