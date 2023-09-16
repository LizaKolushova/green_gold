from django.contrib import admin
from .models import *

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date", "time", "text",)
    list_filter = ("date",)
    search_fields = ("name__startswith",)

@admin.register(BookingEvent)
class BookingEventAdmin(admin.ModelAdmin):
    list_display = ("participant", "event",)
    list_filter = ("event",)
    search_fields = ("event__startswith",)