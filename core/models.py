from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#model for task
class Task(models.Model):

    STATUS_CHOICES = [
        ('pending','Pending'),
        ('in_progress','In Progress'),
        ('completed','Completed'),
        ('on_hold','On Hold'),
    ]

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'tasks')
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length = 200)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'pending')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    