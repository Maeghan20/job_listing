from django.db import models


class jobapp_info(models.Model):
    job_Post= models.CharField(max_length=1000, blank=False)
    job_Company= models.CharField(max_length=1000, blank=False)
    job_Loc= models.CharField(max_length=1000, blank=False)
    job_Shift= models.CharField(max_length=1000, blank=False)
    job_Salary= models.IntegerField()
    
    
    class Meta: 
        db_table= "jobapp"
# Create your models here.


