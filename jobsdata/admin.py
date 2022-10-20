from django.contrib import admin
from . models import Job, Note

class NoteInline(admin.TabularInline):
    model = Note

class NoteAdmin(admin.ModelAdmin):
    model = Note
    list_display = ['note_name']

class JobAdmin(admin.ModelAdmin):
    inlines = [NoteInline]
    model = Job
    list_display = ['position', 'employer']


admin.site.register(Job, JobAdmin)
admin.site.register(Note, NoteAdmin)
