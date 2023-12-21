from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    created = models.DateTimeField()