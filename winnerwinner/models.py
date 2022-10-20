from django.contrib.auth import get_user_model
from django.db import models

class Winner(models.Model):
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
    job_note = models.OneToOneField('Note', default=None, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return (self.position, +","+ self.employer)


class Note(models.Model):
    note_name = models.TextField(default="Applied!", null=True, blank=True)
    # created = models.DateTimeField(auto_now_add=True, blank=True)
    # updated = models.DateTimeField(auto_now_add=True, blank=True)
    related_job = models.ForeignKey('Winner', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.note_name
