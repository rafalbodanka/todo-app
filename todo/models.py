from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=100, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    deadline = models.DateTimeField(null=True)


    def __str__(self):
        return self.title