from django.contrib import admin
from Taches.models import Task
from datetime import timedelta, date
from django.http import  HttpResponse

class TaskAdmin(admin.ModelAdmin):
    list_display=('name', 'description', 'date_begin_task', 'task_closed', 'due_date', 'schedule_date')
    read_only=('created_date')
    
    def colored_due_date(self, request):
        date_due = django_date(self.due_date, "d F Y")
        if self.due_date is None or self.due_date-timedelta(days=7) > date.today():
            
            color = "green"
        elif self.due_date < date.today():
            color ="red"
        else:
            color ="orange"
        return HttpResponse("<span style=color:%s>%s</span>" %(color, self.due_date))
        
    colored_due_date.allow_tags = True

# Register your models here.
admin.site.register(Task, TaskAdmin)