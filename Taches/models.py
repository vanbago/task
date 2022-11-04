from django.db import models
from datetime import datetime , timedelta, date
# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date_begin_task = models.DateTimeField(auto_now_add=True)
    task_closed = models.BooleanField(default=True)
    due_date = models.DateField(null=True)
    schedule_date = models.DateField(default=datetime.now()+timedelta(days=7))
    
    def __str__(self) -> str:
        return self.name
    
    
    
        