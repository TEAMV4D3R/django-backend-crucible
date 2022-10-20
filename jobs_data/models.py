from django.contrib.auth import get_user_model
from django.db import models


class Job(models.Model):
    position = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    status = models.CharField(max_length=256)
    employer = models.CharField(max_length=256)
    notes = models.TextField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="[]", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.position
