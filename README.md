# django-apscheduler-customized
This is a customoized implementation for django-apscheduler as the existing inplementation did not allow save execution details when i schedule a one off job as the job gets deleted when there is no future schedule. Since the job execution model refers job model as foreign key so execution details go missing as soon as the one off job completes execution leaving no trace to check the pos execution status.

