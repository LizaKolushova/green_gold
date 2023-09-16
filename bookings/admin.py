from django.contrib import admin
from .models import *

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ("id", "number", "bio",)
    search_fields = ("bio__startswith",)

@admin.register(Booking)
class BookingtAdmin(admin.ModelAdmin):
    list_display = ("field", "date", "time")
    list_filter = ("field",)