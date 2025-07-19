from django.contrib import admin
from .models import Event


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display= ('title','date','location','created_by')
    list_filter= ('date',)

admin.site.register(Event, EventAdmin)
