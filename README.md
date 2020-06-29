# django-apscheduler-customized
This is a customoized implementation for django-apscheduler as the existing inplementation did not allow saving execution details in case of one off jobs as the job gets deleted when there is no future schedule. Since the job execution model refers job model as foreign key so execution details go missing as soon as the one off job completes execution leaving no trace to check the pos execution status. The job deletion is done by apscheduler module which i did not want to override for hygein and code sanity hence hacked the django apscheduler app in-stead.

This has been overcome by creating an additonal copy of job model which is then referred as foreign key for execution model and hence does not remove trace when the original job finishes.


### Start the server
It is done when django application is loaded. See apps.py for code reference.

### Schedule a one off job
```
#Add function to run at a certain time only once
from apps import scheduler
from datetime import datetime, timedelta

def foo(message, who):
    print(f"Hi {who.lower()}, {message}")

release_datetime =  datetime.now() + timedelta(hours=5)
scheduler.add_job(foo, 'date', name="foo_run", misfire_grace_time=300, run_date=release_datetime, args=["Bar", "How are you"])
```
