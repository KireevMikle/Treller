from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=[('todo', 'To do'), ('inwork', 'In work'), ('done', 'Done')], default='todo')
    priority = models.CharField(max_length=100, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium')
    date_limit = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='tasks')


class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)