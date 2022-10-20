from django.contrib import admin
from . models import Winner, Note

class NoteInline(admin.TabularInline):
    model = Note

class NoteAdmin(admin.ModelAdmin):
    model = Note
    list_display = ['note_name']

class WinnerAdmin(admin.ModelAdmin):
    inlines = [NoteInline]
    model = Winner
    list_display = ['position', 'employer']


admin.site.register(Winner, WinnerAdmin)
admin.site.register(Note, NoteAdmin)
