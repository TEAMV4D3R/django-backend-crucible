from django.contrib import admin
from .models import Officer, Rank, Ship


class OfficerTabularInline(admin.TabularInline):
    model = Officer


class OfficerAdmin(admin.ModelAdmin):
    model = Officer
    list_display = ['name', 'rank']


class ShipAdmin(admin.ModelAdmin):
    inlines = [OfficerTabularInline]
    model = Ship
    list_display = ['name', 'registry']


class RankAdmin(admin.ModelAdmin):
    model = Rank
    list_display = ['name']

# Register your models here.
admin.site.register(Officer, OfficerAdmin)
admin.site.register(Rank, RankAdmin)
admin.site.register(Ship, ShipAdmin)
