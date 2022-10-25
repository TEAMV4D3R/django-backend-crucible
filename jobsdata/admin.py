from django.contrib import admin
from . models import Job

class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display = ['position', 'employer']


admin.site.register(Job, JobAdmin)
