from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Active_job(models.Model):
    position = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    company = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.position
