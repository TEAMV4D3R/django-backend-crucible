from django.contrib.auth import get_user_model
from django.db import models

class Job(models.Model):
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    position = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    employer = models.CharField(max_length=256)
    status = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True)
    note_name = models.TextField(default="Applied!", null=True, blank=True)

    def __str__(self):
        return (f"{self.position}, {self.employer}")
