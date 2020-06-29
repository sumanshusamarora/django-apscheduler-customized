# django-apscheduler-customized
This is a customoized implementation for django-apscheduler as the existing inplementation did not allow saving execution details in case of one off jobs as the job gets deleted when there is no future schedule. Since the job execution model refers job model as foreign key so execution details go missing as soon as the one off job completes execution leaving no trace to check the pos execution status. The job deletion is done by apscheduler module which i did not want to override for hygein and code sanity hence hacked the django apscheduler app in-stead.

This has been overcome by creating an additonal copy of job model which is then referred as foreign key for execution model and hence does not remove trace when the original job finishes.
