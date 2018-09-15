from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length = 200)
    task_created = models.DateTimeField('Created', '', auto_now_add=True)
    task_due_on = models.DateTimeField('Due on')
    task_owner = models.CharField('Owner',max_length=200)
    task_done = models.NullBooleanField('Done')

    def __str__(self):
        return self.task_title
            
        


    
